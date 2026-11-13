#!/usr/bin/env python3
"""Genera chiavi Ed25519 sul PC del proprietario; non caricare mai la chiave privata."""
from pathlib import Path
from getpass import getpass
import os

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import (
    Encoding, PrivateFormat, PublicFormat, BestAvailableEncryption,
)

def main():
    target = Path.home() / ".config" / "archivio-nupo" / "firma"
    target.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(target, 0o700)
    private_file = target / "privata_ed25519.pem"
    public_file = target / "pubblica_ed25519.pem"
    if private_file.exists() or public_file.exists():
        raise SystemExit("Chiavi gia' presenti: non sovrascrivo. Conserva il backup offline.")
    password = getpass("Passphrase robusta per la chiave privata (minimo 12 caratteri): ")
    confirm = getpass("Ripeti la passphrase: ")
    if len(password) < 12 or password != confirm:
        raise SystemExit("Passphrase non coincidenti o troppo corte. Nessuna chiave creata.")
    private_key = Ed25519PrivateKey.generate()
    content = private_key.private_bytes(
        Encoding.PEM, PrivateFormat.PKCS8,
        BestAvailableEncryption(password.encode("utf-8")),
    )
    fd = os.open(private_file, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as handle:
        handle.write(content)
    public_file.write_bytes(private_key.public_key().public_bytes(
        Encoding.PEM, PublicFormat.SubjectPublicKeyInfo,
    ))
    os.chmod(public_file, 0o644)
    print("Chiave pubblica:", public_file)
    print("Chiave privata cifrata:", private_file)
    print("Conserva la passphrase e una copia offline cifrata; NON inviarle a nessuno.")

if __name__ == "__main__":
    main()
