# Formato manifesto firmato — schema 1 (informativo)

Esempio **illustrativo e non firmato**, NON valido per l'installazione:

```json
{
  "schema": 1,
  "app": "archivio-nu-po",
  "version": "0.3.9",
  "tag": "v0.3.9",
  "channel": "beta",
  "packages": [
    {
      "platform": "ubuntu",
      "filename": "archivio-nupo-ubuntu.zip",
      "size": 1234567,
      "sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    }
  ]
}
```

Il manifesto reale contiene anche `signature`: firma Ed25519 in Base64
del JSON senza il campo `signature`, serializzato con chiavi ordinate,
UTF-8, `ensure_ascii=False`, separatori `,:` e senza NaN.

Il client 0.3.8 contiene il verificatore e i limiti relativi a schema,
formato, piattaforme, firme, dimensioni e SHA-256: la descrizione qui e'
documentazione, non sostituisce il verificatore reale.

**Non pubblicare mai un manifesto d'esempio come `updates.json`.**
