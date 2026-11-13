# Protocollo di pubblicazione per Archivio NU·PO

## 1. Preparazione (da effettuare una sola volta)
- Generare una coppia Ed25519 sul PC proprietario con il programma
  `strumenti_release/genera_chiavi.py` compreso nella candidata 0.3.8.
- Non caricare mai la chiave privata su questo repository e conservarne una
  copia di sicurezza cifrata, offline.
- Inserire la chiave pubblica affidabile nel programma **prima** di abilitare
  qualsiasi aggiornamento automatico.
- Preparare e collaudare **due veri pacchetti**, Ubuntu e Windows,
  mantenendo separati programma, profili, originali e dati dell'archivio.

## 2. Preparazione di una release
- Definire versione a tre numeri (es. 0.3.9) e canale `beta` o `stable`.
- Calcolare SHA-256 e dimensioni effettive dei pacchetti.
- Generare `updates.json` con `strumenti_release/firma_release.py`
  e firma privata offline. Verificare con `controlla_manifesto.py`.
- Creare una GitHub Release con tag `vX.Y.Z` e allegare soltanto i
  pacchetti collaudati e il manifesto firmato.
- Per ora l'operazione di pubblicazione delle Release e' MANUALE;
  la disponibilita' di questo repository da sola non attiva distribuzione
  ne' installazione sui terminali.

## 3. Controllo sui terminali (non ancora attivo)
- All'avvio e alla riconnessione verificare se esiste una versione piu' nuova.
- I dati GitHub non firmati possono solo segnalare possibili aggiornamenti.
- Scaricare il manifesto e validarne firma, schema, canale, piattaforma,
  versione e anti-downgrade.
- Scaricare in una cartella temporanea, confrontare dimensione e SHA-256,
  quindi applicare l'aggiornamento solo a programma chiuso.
- Eseguire copia di sicurezza e snapshot dati prima di eventuali migrazioni,
  con ripristino della versione precedente se il test fallisce.

## 4. Requisiti prima dell'attivazione
- Chiave pubblica fissata nel software.
- Programma capace di scoprire, scaricare e verificare Release via HTTPS.
- Installer atomico per Ubuntu/Windows con rollback.
- Collaudi delle migrazioni, dell'installazione e del ripristino sui sistemi reali.
- Monitoraggio dell'errore senza inviare dati personali.
- Nessuna interferenza con RadioD1-Gateway e i suoi servizi.

**Stato al 13 novembre 2026:** repository creato, nessuna release firmata
pubblicata e aggiornamento automatico non abilitato.
