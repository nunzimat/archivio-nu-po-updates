# Archivio NU·PO — aggiornamenti software

Repository **pubblico, dedicato esclusivamente** alla futura distribuzione
degli aggiornamenti per Archivio NU·PO su Ubuntu e Windows.

**Stato:** preparazione tecnica in corso. **Non sono ancora pubblicate
release firmate abilitate per l'aggiornamento automatico.**

- Le release del software saranno distribuite mediante GitHub Releases.
- Prima di accettare qualsiasi aggiornamento, i terminali dovranno
  verificare la firma Ed25519 di `updates.json` e gli SHA-256 dei pacchetti.
- La chiave privata di firma rimane sul computer del proprietario;
  qui non saranno pubblicati segreti, font proprietari, dati degli archivi,
  password, immagini private o documenti del Vocabolario.
- I dati dell'archivio resteranno separati dagli eseguibili e protetti
  da backup e migrazioni controllate.
- Il canale beta sarà collaudato prima di abilitare il canale stabile.

Documentazione:
- [Protocollo di pubblicazione](docs/PROTOCOLLO_PUBBLICAZIONE.md)
- [Formato del manifesto](docs/SCHEMA_MANIFESTO.md)
- [Sicurezza](SECURITY.md)

**RadioD1-Gateway non fa parte di questo progetto.**
