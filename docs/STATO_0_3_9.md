# Stato infrastruttura aggiornamenti — candidata 0.3.9

- Repository GitHub attivo: `nunzimat/archivio-nu-po-updates`.
- La chiave pubblica Ed25519 dell'amministratore e' pubblicata in `keys/pubblica_ed25519.pem`.
- SHA-256 **del PEM**:
  `30611f83d6c76d870a35fb0700fef6fb64f8f55e77a2938167d8c7cb9005bb03`.
- La candidata 0.3.9 incorpora una copia della stessa chiave, verificata mediante SHA-256
  fissato nel codice. La verifica NON preleva la chiave dal repository.
- In `Impostazioni → Aggiornamenti` l'amministratore puo' eseguire un controllo
  **manuale** delle release beta firmate con Ed25519.
- La richiesta API GitHub e' usata solo come indice. Il programma rifiuta
  manifesti non firmati dalla chiave incorporata, pacchetti non autorizzati,
  SHA-256 incongruenti e tentativi di downgrade.
- La candidata 0.3.9 NON scarica ne' installa automaticamente il programma;
  sincronizzazione cloud e aggiornamento dei terminali restano inattivi.
- Le chiavi private e le passphrase devono rimanere ESCLUSIVAMENTE sul computer
  del proprietario. Non vanno mai caricate su GitHub o nelle release.
- L'archivio personale, i font proprietari e i profili non devono essere pubblicati.

## Passaggi ancora necessari
1. Creare i veri pacchetti Ubuntu/Windows (distribuibili senza dati privati).
2. Firmare `updates.json` sul computer con la chiave privata.
3. Pubblicare una beta firmata come GitHub Release e collaudarne il rilevamento.
4. Progettare e collaudare transazioni di installazione, backup e rollback prima
   di abilitare l'aggiornamento automatico sui terminali.

Non considerare una copia del pacchetto beta come una release stabile.
