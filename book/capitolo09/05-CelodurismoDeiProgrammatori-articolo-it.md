# Il "celodurismo" dei programmatori

Nel mondo della programmazione, esiste un fenomeno curioso che potremmo definire "celodurismo". Questo termine descrive un atteggiamento di ostinata resistenza all'evoluzione degli strumenti e delle pratiche di sviluppo software.

Un tempo, quando le risorse erano scarse e preziose, i programmatori dovevano essere incredibilmente ingegnosi per spremere ogni goccia di potenza dai loro sistemi. Questa necessità ha forgiato abitudini e mentalità che, in alcuni casi, sono sopravvissute ben oltre la loro utilità pratica, trasformandosi in una sorta di folklore professionale.

```text
640K ought to be enough for anybody
```

Questa celebre frase attribuita a Bill Gates, anche se lui ne ha negato la paternità, rappresenta bene l'atteggiamento di molti "celoduristi" nei confronti dell'innovazione tecnologica. Per questi programmatori, l'idea di utilizzare strumenti moderni come IDE avanzati, debugger grafici o assistenti AI sembra quasi un'eresia, una violazione dei principi fondamentali della programmazione "vera", un sintomo di debolezza e incapacità.

## Le radici storiche

Negli albori dell'informatica, quando i computer venivano alimentati a colpi di schede perforate, programmare significava lavorare con sistemi dotati di memoria e processori limitati. I programmatori dell'epoca dovevano essere veri e propri artisti dell'ottimizzazione, capaci di scrivere codice che fosse al contempo funzionale ed estremamente efficiente.

Questa era ha prodotto capolavori di ingegnosità, e pratiche che ancora sopravvivono in ambienti dotati di scarse risorse: avete mai provato a programmare per microcontrollori o sistemi embedded? Qui, ogni byte di memoria e ogni ciclo di clock contano, e l'arte dell'ottimizzazione vive ancora di ottima salute, anche se più di una crepa inizia a vedersi all'orizzonte.

Col passare del tempo e l'evoluzione dell'hardware, molte di queste limitazioni sono venute meno, ma l'etica del "fare di più con meno" è rimasta profondamente radicata nella cultura della programmazione, talvolta trasformandosi in un atteggiamento di resistenza verso strumenti e pratiche che potrebbero semplificare e velocizzare il lavoro di sviluppo.

```text
"Il codice più efficiente è quello che non devi scrivere"
```

## Il manifesto del celodurismo

Per capire che tipo di programmatori siete, ecco un piccolo test per valutare il vostro grado di "purezza". 
Provate a capire quanto siete a favore o a sfavore di queste affermazioni:

### 1. L'IDE non serve a nulla

Un programmatore deve essere spartano: meno strumenti usa, più è sinonimo di competenza

```text
"Per scrivere del codice mi basta Notepad (o Vi) e la CLI"
```

Questa affermazione è spesso pronunciata con un misto di orgoglio e nostalgia. Chi la sostiene sembra voler comunicare: "Sono un vero programmatore, non ho bisogno di aiuti". Questa posizione ignora deliberatamente i vantaggi offerti dagli IDE moderni.

Personalmente ho visto programmatori usare comandi come:

```text
copy con: pippo.prg
```

con lo stesso orgoglio di chi a scuola prende un ottimo voto.

Non sottovalutiamo però i vantaggi degli IDE moderni e come come prima cosa leviamoci dalla testa che gli IDE siano dei semplici editor di testo con qualche abbellimento. Sono potenti strumenti che integrano numerose funzionalità per migliorare la produttività e la qualità del codice:

- Debugging: Punti di interruzione, ispezione e alterazione delle variabili in tempo reale, esecuzione passo-passo del codice, call stack e molto altro.
- Refactoring: Rinominare variabili o funzioni in tutto il progetto con un solo click, estraendo metodi o riorganizzando il codice in modo sicuro.
- Analisi statica: Identificazione di potenziali bug, violazioni di stile o pattern problematici prima dell'esecuzione.
- Integrazione con sistemi di versionamento: Gestione di branch, commit e merge direttamente dall'interfaccia dell'IDE.
- Supporto per framework e librerie: Autocompletamento, non delle sole librerie base, ma anche suggerimenti specifici per i framework utilizzati nel progetto.

Questi sono solo alcuni dei motivi per i quali, quando entro in un editor inventato negli anni '70, mi sento come se mi avessero tolto un braccio.

Per onestà intellettuale non possiamo negare che, in alcune situazioni, un IDE potrebbe essere eccessivo, quando ad esempio occorre fare una modifica rapida o quando si lavora su sistemi remoti con risorse limitate. In questi casi editor minimali o qualsiasi cosa che apre una console testuale, potrebbero essere la scelta migliore.
Per il lavoro di tutti i giorni e per progetti di una certa complessità, rifiutare categoricamente l'uso di un IDE moderno significa privarsi di strumenti che possono significativamente migliorare la qualità del codice e la produttività del programmatore e dell'intero team (si, perché il codice non è solo tuo, ma di tutti quelli che ci lavorano).

### 2. La CLI è la soluzione a tutti i problemi

Non nascondiamoci dietro a un dito, la CLI ha un fascino innegabile. Anni di film con hacker piegati su tastiere meccaniche e schermi neri con scritte verdi hanno formato generazioni di programmatori. Cosa c'è di più potente che controllare un computer digitando comandi testuali?
Questo approccio, anche se ha il fascino della prima ragazza incontrata al liceo, ha una serie di limiti che spesso vengono trascurati:

- Curva di apprendimento: Memorizzare pochi comandi è facile, memorizzarne decine o centinaia di comandi, con tutte le loro opzioni può essere scoraggiante per i neofiti e per chi non usa la CLI quotidianamente.
- Visualizzazione dei dati: Alcune informazioni sono semplicemente più facili da comprendere quando presentate graficamente.
- Operazioni complesse: Certe attività, come la gestione di branch in un repository Git, possono diventare molto più intuitive con una rappresentazione visuale.

Git è un ottimo esempio di come CLI e GUI possano coesistere e completarsi a vicenda. Mentre la CLI di Git offre un controllo granulare e la possibilità di automatizzare operazioni attraverso script, strumenti GUI come le integrazioni in VSCode possono rendere più accessibili operazioni complesse come:

- Visualizzare la storia dei commit con un grafico delle branch
- Effettuare rebase interattivi
- Risolvere conflitti di merge con strumenti di diff visuale

Come sempre la verità sta nel mezzo e l'approccio più saggio è quello di padroneggiare entrambi gli strumenti. Usare la CLI per operazioni rapide e per creare script automatizzati, ma non si deve esitare a passare a una GUI quando questa può offrire una visione più chiara o un flusso di lavoro più efficiente.

### 3. Non usiamo Windows perché i programmatori usano Linux (o MacOS)

Ormai non conto più le notti che ho passato a leggere e commentare le "guerre di religione" dei sistemi operativi.

```text
"Winzoz" on funziona
Sarà bello Linux che ha 200 versioni e tutte incompatibili
Lasciate stare, con MacOS funziona tutto
Guarda che Apple ti fa pagare il doppio di quello che vale quel computer
```

Si potrebbe andare avanti all'infinito, creando flame pieni di odio e carichi di ignoranza, ma la realtà è che ogni sistema operativo ha i suoi pregi e difetti, ed è sbagliato sostenere che uno sia superiore agli altri in modo assoluto.

Un programmatore dovrebbe essere superiore a queste chiacchiere da bar. Questo non limita la sua libertà di sentirsi a suo agio su un sistema piuttosto che su un altro, ma è assolutamente controproducente mettersi i paraocchi e ignorare l'esistenza di altri sistemi operativi oltre a quello preferito.

Ragioniamo poi sul fatto di lavorare giornalmente su piattaforme differenti e dei vantaggi che questo approccio può portare:

- Cross-platform: Sviluppare e testare su più piattaforme assicura che il software funzioni correttamente per un'ampia base di utenti. "Write once, run anywhere" è un obiettivo importante per molte applicazioni e anche se di base i linguaggi assicurano che questa cosa possa essere vera, ogni programmatore ci mette del suo per fare in modo che non lo sia.
- Flessibilità: Molte aziende utilizzano ambienti misti e la capacità di adattarsi è un vantaggio competitivo.
- Comprensione delle differenze: Lavorare su diversi sistemi aiuta a comprendere meglio le peculiarità di ciascuno, migliorando la capacità di debug e ottimizzazione.

Invece di legarsi dogmaticamente a un singolo sistema operativo, un approccio più produttivo è quello di scegliere lo strumento giusto per il lavoro giusto, mantenendo la flessibilità di muoversi tra diverse piattaforme quando necessario.

### 4. Il debugger è per i deboli

Sfatiamo un'idea

```text
Un "vero programmatore" scrive codice perfetto al primo tentativo
```

Questa storiella gira nel mondo della programmazione da anni. Più o meno tutti i programmatori famosi si sono cuciti addosso questa immagine, e ognuno di noi è pronto a raccontarla a fine serata quanto le birre sono ormai finite.
La realtà è che il debug e i test sono una parte essenziale ed inevitabile del processo di sviluppo software e questa mentalità di resistenza all'uso di strumenti di debug, vedendoli come una sorta di "stampella", è qualcosa che va superato.

Ormai non conto più le volte che ho preso in mano un software considerato "concluso", pieno i test funzionanti, e piano piano sono usciti fuori problemi, casi d'uso non coperti, problemi di analisi e progettazione: no, l'illusione che la prima stesura di un programma sia in grado di generare un software perfetto e che i test bastino per capire cosa funziona o non funziona è solo un'illusione.

In queste situazioni: log, debug e nuovi test diventano necessari per capire cosa non funziona e come risolverlo.

### 5. Il codice è tutto nella mia testa

L'analisi, la condivisione della conoscenza e la documentazione sono aspetti spesso trascurati nella programmazione.

```text
Ho tutto in testa
```

Non esiste una frase meno produttiva di questa, che atrofizza qualsiasi tipo di discussione e di collaborazione.

Esiste una narrativa romantica del programmatore come genio solitario, capace di tenere interi sistemi complessi nella propria mente e di vedere il proprio software come Neo vedeva Matrix.
Questo approccio ha un errore di base: la mente umana, seppur meravigliosa, ha limiti nella quantità di informazioni che può mantenere.

Non tutti siamo Dennis Nedry, il programmatore di Jurassic Park che sapeva tutto il codice del parco a memoria e, anche se lo fossimo, ricordiamoci che fine ha fatto.

Dimenticare il passato è una forma di protezione che viene attivata dal nostro cervello per evitare di impazzire. Questo è il motivo per cui è importante documentare il codice, condividere la conoscenza e lavorare in team.

Ma anche se la propria mente avesse una capacità infinita, ci sono altri motivi per cui il "codice nella mia testa" è un problema:

- Collaborazione: Se il funzionamento del codice è chiaro solo nella mente di chi l'ha scritto, diventa difficile per altri contribuire o mantenere il progetto.
- Propensione agli errori: Senza una documentazione chiara o commenti nel codice, è facile dimenticare dettagli importanti o fare assunzioni errate.
- Onboarding complicato: Nuovi membri del team avranno difficoltà a comprendere e contribuire al progetto.

Occorre quindi che il "celodurista" si renda conto che il codice è un prodotto collaborativo e non condividere delle informazioni non è il miglior approccio per mantenere il proprio lavoro, quanto il modo migliore per perderlo.

Spingiamo quindi questi programmatori a documentare, scrivere Wiki, fare code review, usare diagrammi e schemi, in modo da condividere la conoscenza.

Un approccio che valorizza la documentazione e la condivisione della conoscenza non solo rende il progetto più robusto e mantenibile, ma contribuisce anche alla crescita professionale di tutto il team.

### 6. I programmatori non usano ChatGPT

Diciamocelo: le intelligenze artificiali sono tutto, fuorché intelligenti.

```text
Guarda quanti errori fa ChatGPT, non può sostituire un programmatore
```

Le allucinazioni, ma soprattutto l'uso scorretto e superficiale delle AI, porta molti programmatori a pensare che siano strumenti non utilizzabili.
No, le AI non sono motori di ricerca, sono strumenti di aggregazione linguistica, che possono apprendere il nostro contesto di lavoro, e come tali vanno usate.

A queste teoria si sovrappongono sempre di più le teorie che in futuro le AI sostituiranno i programmatori.
Il programmatore "duro e crudo" non usa quindi questi strumenti, perché non ne ha bisogno, perché non funzionano, perché "io sono meglio".

Tutto vero, ma solo in parte. La realtà è che le AI sono strumenti che possono aiutare i programmatori a scrivere codice più velocemente e con meno errori, ma non basta un ora per arrivare a questo risultato, occorrono settimane di utilizzo per capire al meglio come usare questo strumento ed individuare al volo pregi e difetti.

L'AI deve essere vista come strumento di potenziamento, come l'evoluzione dell'autocompletamento dei moderni IDE, ma in grado di estendere il completamento a un contesto più ampio e complesso.

Ho visto di recente il film Atlas, non per Jennifer Lopez, come molti di voi saranno propensi a pensare, ma per arricchire la mia testa di nuove immagini su futuri possibili. All'interno di questo film l'AI viene vista come un completamento del lavoro dell'uomo ed entrambi si migliorano e potenziano, lavorando in simbiosi.

Per chi ha passato i pomeriggi della propria infanzia a guardare Star Trek: è l'evoluzione della fusione mentale dei vulcaniani o del simbionte dei Trill.

Ci sono molti aspetti della vita di un programmatore che traggono vantaggio da una AI

- Generazione di boilerplate: L'AI può rapidamente produrre strutture di codice di base, permettendo ai programmatori di concentrarsi sugli aspetti più complessi e creativi.
- Debugging assistito: Modelli come ChatGPT possono aiutare a identificare errori nel codice e suggerire possibili soluzioni.
- Esplorazione di nuove tecnologie: L'AI può fornire spiegazioni e esempi di utilizzo per framework o librerie con cui il programmatore non ha familiarità.
- Ottimizzazione: Suggerimenti per migliorare l'efficienza o la leggibilità del codice.
- Test: Generazione di test automatici per verificare il corretto funzionamento del proprio lavoro.

Invece di rifiutare categoricamente l'uso delle AI, i programmatori dovrebbero considerarle come strumenti che possono migliorare la loro produttività e la qualità del loro lavoro.

## Conclusioni

Il "celodurismo" nella programmazione, seppur radicato nella storia come simbolo di ingegnosità e ottimizzazione, rischia di diventare un freno all'innovazione e all'efficienza nel mondo dello sviluppo software moderno.

Un approccio più equilibrato riconosce il valore della tradizione e dell'esperienza, ma rimane aperto alle nuove tecnologie e metodologie che possono migliorare il processo di sviluppo.

Il vero segno di un programmatore esperto non è l'adesione dogmatica a pratiche del passato, ma la capacità di valutare criticamente e adottare gli strumenti e le pratiche più adatte a ogni situazione specifica.

Ammiro i celoduristi per la loro tenacia, ma sono sicuro che se avessero più coraggio potrebbero trarre grandi vantaggi da una rivalutazione delle loro posizioni.
