# Sicurezza degli aggiornamenti — Archivio NU·PO

Questo repository e' pubblico e serve **solo** alla distribuzione del software.

## Stato attuale
- **Non esiste ancora una release verificata e firmata per l'aggiornamento automatico.**
- L'aggiornamento automatico del programma non e' abilitato.
- Il modulo di verifica e firma Ed25519 e' predisposto nella candidata 0.3.8,
  ma deve ancora essere collegato a una chiave pubblica fissata nel client,
  alla ricerca online delle nuove versioni e a un installer con rollback.

## Regole obbligatorie
1. La chiave privata Ed25519 viene generata sul computer del proprietario,
   protetta con passphrase e conservata **solo localmente/offline**.
   NON caricarla su GitHub, nei GitHub Secrets, nelle chat o nei pacchetti.
2. I terminali conoscono la chiave pubblica da un'installazione fidata
   precedente. Non sostituirla scaricandola dal medesimo server delle release.
3. Ogni aggiornamento utilizza un manifesto `updates.json` firmato,
   contenente nome, piattaforma, versione, lunghezza e SHA-256 del pacchetto.
4. Verificare firma **prima** di fidarsi del manifesto e SHA-256 + dimensione
   **prima** di eseguire il pacchetto. Un puntatore «ultima versione» non
   autenticato serve solo a scoprire candidati, mai ad autorizzare installazioni.
5. Il software non deve mai sovrascrivere archivi dati, credenziali o backup.
   Richiedere snapshot, migrazioni transazionali e possibilita' di rollback.
6. Non distribuire font proprietari (SophoMOD OMIPA), dati di dizionario,
   esempi/ODT personali, fotografie, credenziali cloud o archivi dell'utente.
7. Nessuna release e' «stabile» finche' i test Ubuntu e Windows non sono
   stati eseguiti e registrati. Seguire un canale beta distinto.

## Segnalazioni
Non inserire segreti in issue pubbliche. Per segnalazioni sensibili,
contattare direttamente il proprietario del repository con un canale privato.
