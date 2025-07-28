# E se l'anello debole della programmazione fosse il programmatore stesso?

Mentre le intelligenze artificiali promettono di rivoluzionare lo sviluppo software accelerando ogni fase del processo, emerge un paradosso inquietante: il programmatore stesso potrebbe essere diventato il principale ostacolo alla velocità che il mercato richiede. In un ecosistema dove l'automazione genera codice a ritmi inimmaginabili, la supervisione umana introduce latenze, controlli e rallentamenti che contraddicono l'obiettivo primario dell'efficienza.

## Un po' di storia

Proviamo a capire il mondo della programmazione, riflettendo su una normale evoluzione di progetto e pensando a come un programmatore si muove nel tempo.

Quando iniziamo a muovere i primi passi in questo mondo, iniziamo a studiare i primi linguaggi e a studiare i primi componenti, librerie e framework che possono aiutarci nel nostro lavoro.
Lo studio delle best practice e la conoscenza sempre più profonda degli strumenti utilizzati tende a focalizzare il nostro lavoro in una strada conosciuta che tendiamo a replicare, in parte o totalmente, in ogni nuovo progetto.

Se riflettiamo sulla programmazione, spesso è un processo lineare: oggi realizziamo una data entry funzionante, domani implementiamo controlli efficienti, poi ragioniamo su meccanismi di astrazione dei dati, creiamo delle API, ottimizziamo le performance, aumentiamo le misure di sicurezza e così via.
Ogni progetto diventa la sommatoria delle esperienze precedenti, opportunamente riorganizzate: forse meglio progettare le API da subito, la sicurezza sarebbe meglio metterla come primo passo, usiamo una libreria di controlli consolidata, questo servizio di autenticazione e così via. La sommatoria di esperienze, in un'ottica di evoluzione continua, può però nascondere una trappola insidiosa.

## Il peso crescente della complessità

Il vero problema non risiede nel codice stesso, ma nella complessità che si accumula inesorabilmente nel tempo. Ogni nuovo progetto rappresenta un punto di partenza che raramente è davvero nuovo: il programmatore inserisce immediatamente tutto ciò che ha appreso negli anni precedenti, accumulando inconsapevolmente strati di complessità.

Inizialmente questa complessità appare governabile, ma si trasforma progressivamente in un peso sempre più difficile da sostenere. Ogni nuova funzionalità, ogni bug da correggere, ogni richiesta del cliente aggiunge un ulteriore strato che si sedimenta sul codice esistente, creando una stratificazione che richiede competenze sempre più specializzate per essere gestita.

Questa dinamica si scontra frontalmente con le aspettative del mercato attuale, dove la velocità è diventata il parametro dominante. I clienti vogliono tutto e subito:

```text
Realizza un sito web come quello di Apple, ma in una settimana dato che hai tutto pronto.
Il prototipo deve essere pronto per stasera
Il bug deve essere risolto entro oggi
```

e per finire con una citazione che avrò sentito un numero infinito di volte:

```text
Per quando la vuoi questa feature?
Per ieri!
```

La pressione temporale, da sempre presente, diventa sempre più costante e ineludibile.

## L'illusione della compressione temporale

Di fronte a questa pressione, l'industria ha tentato diverse strategie di automazione. In passato esistevano i CASE (Computer-Aided Software Engineering), fabbriche di codice specializzate per specifiche categorie di problemi. Con l'evoluzione delle esigenze, questi strumenti si sono trasformati nei framework moderni: più flessibili e general-purpose rispetto alla verticalità dei CASE, ma ancora complessi e non sempre intuitivi nell'utilizzo.

L'arrivo delle intelligenze artificiali ha rappresentato la promessa definitiva: programmi che scrivono codice per noi, che risolvono problemi automaticamente, che permettono di risparmiare tempo e fatica. Tuttavia, questa apparente soluzione si scontra con una realtà ineluttabile: il programmatore rimane il controllore di questo processo: un controllore umano, con tutte le sue limitazioni e i suoi tempi di reazione.

Anche delegando la scrittura del codice all'AI, persistono tempi irriducibili: apprendimento, adattamento, debug, test e supervisione umana. Fino a quando questa supervisione rimarrà necessaria, il tempo complessivo non potrà essere drasticamente ridotto. È proprio in questa dinamica che emerge il programmatore come potenziale anello debole: l'elemento umano che introduce overhead e latenze nel processo di automazione.

## Ma come le AI ci stanno aiutando e si stanno evolvendo?

Il 2025 è stato l'anno del "vibe coding": programmazione assistita dall'intelligenza artificiale dove ogni problema viene risolto attraverso prompt iterativi. Se qualcosa non funziona, si genera un nuovo prompt; se occorre modificare qualcosa, un altro prompt ancora.

Questa evoluzione ha trasformato l'AI da semplice strumento di supporto a principale strumento di lavoro.

Lavoro ormai da mesi in modalità "Vibe", prima con prompt inseriti nelle varie LLM, poi tramite Copilot, poi con strumenti CLI come Gemini e Copilot Agent, fino ad arrivare a strumenti più avvolgenti.

Dopo un po' che ci sbatti la testa inizi a vederne i limiti e le incongruenze, anche se spesso pensi siano più tuoi che della macchina che stai usando.

Come me, anche altre figure di spicco, come Jack Dorsey, hanno iniziato a utilizzare l'AI per i propri "progetti del weekend", realizzando applicazioni come BitChat interamente attraverso codice generato automaticamente.

L'esperienza diretta con questi strumenti rivela però una dinamica complessa. Affidarsi completamente al "vibe" per generare grandi porzioni di codice produce un numero elevato di elementi da ricontrollare e sistemare. La capacità interpretativa dell'AI, pur impressionante, può facilmente deviare dalla direzione prevista.

L'approccio più efficace si è rivelato quello della frammentazione: utilizzare l'AI per piccoli task specifici, controllare e testare ogni componente, quindi assemblarli manualmente. Questo metodo permette di mantenere il controllo qualitativo pur sfruttando l'accelerazione offerta dall'automazione. È analogo al processo di addomesticamento: occorre conoscere, comprendere e guidare lo strumento prima di poterlo utilizzare efficacemente.

## Quando il programmatore si ferma: scenario futuro prossimo

La crescente accelerazione dei processi di sviluppo pone una questione critica: cosa accade quando il programmatore non è disponibile? In passato, l'assenza di uno sviluppatore comportava semplicemente un rallentamento proporzionale. I cicli di rilascio erano annuali, la pressione per nuove funzionalità limitata.

Nel presente, l'accelerazione ha trasformato ogni interruzione in un potenziale problema sistemico. Nel futuro prossimo (2-3 anni), è plausibile che i progetti continuino a evolvere in modo non supervisionato durante l'assenza del programmatore, con l'AI che genera autonomamente codice, risolve issue e gestisce branch.

Al ritorno, il programmatore si troverebbe di fronte a decine di branch da esaminare, issue da comprendere, bug da analizzare per verificare la correttezza del codice generato automaticamente. Il carico mentale di questa situazione è significativo: senso di colpa per l'assenza, ansia da supervisione mancata, pressione per recuperare il controllo di un processo che ha continuato a evolversi autonomamente.

Questo scenario può facilmente degenerare in un circolo vizioso di burnout, abbandono dell'azienda o perdita di interesse professionale, riassumibile nell'atteggiamento pericoloso:

```text
"Accettiamo questa pull request, tanto l'AI ha già fatto tutto il lavoro, cosa può andare storto?"
```

## Il futuro del programmatore: oltre il presente immediato

Proiettandoci di alcuni anni nel futuro, l'evoluzione del ruolo del programmatore appare inevitabile. L'AI supera già qualsiasi digitatore in velocità, inizia a produrre codice di qualità superiore a quello di molti sviluppatori, e può commettere errori a una velocità senza precedenti. Tuttavia, rimane potenza pura senza pensiero strategico.

La trasformazione del ruolo del programmatore seguirà probabilmente questa traiettoria: meno tempo dedicato alla scrittura diretta di codice, più tempo nell'interazione con le AI e nel lavoro orientato al business. Questo cambiamento richiederà consapevolezza e preparazione adeguata, poiché stravolgerà completamente l'attuale concezione della programmazione, spingendo i professionisti oltre le competenze attuali.

In questo nuovo paradigma, una persona descriverà un problema in poche frasi e un modello linguistico specializzato nell'analisi genererà i prompt per un modello specializzato nella scrittura del codice. Il programmatore evolverà da codificatore manuale a guida, tester e, forse, perfezionatore del codice generato dall'AI.

Questa trasformazione comporterà la scomparsa di alcune pratiche attuali: il debug tradizionale, la necessità di documentare minuziosamente il codice, l'importanza di variabili con nomi esplicativi. Parallelamente, emergeranno probabilmente nuovi linguaggi di programmazione progettati per l'interpretazione da parte delle macchine piuttosto che per la leggibilità umana.

## La mente umana: il limite invalicabile

In questo scenario di accelerazione continua, efficienza spinta e automazione forsennata, esiste un elemento che non può essere compresso: la mente umana. Plasmata da milioni di anni di evoluzione, la nostra mente ha sviluppato meccanismi per risolvere problemi complessi attraverso processi lenti e ponderati.

Privare questa "macchina biologica" del tempo necessario per elaborare informazioni e sovraccaricarla di input continui produce un solo risultato: il blocco funzionale. In un mondo dove ogni rallentamento genera effetti domino disastrosi, prendersi giorni di malattia o di riposo rischia di diventare un lusso inaccessibile.

Nelle organizzazioni strutturate inadeguatamente, dove ogni persona è singolarmente responsabile di specifiche attività senza adeguata distribuzione dei carichi di lavoro, il peso mentale e fisico che ogni programmatore deve sostenere diventerà progressivamente insostenibile.

## Conclusioni: l'anello debole che può spezzare la catena

La programmazione sta attraversando una trasformazione epocale con l'avvento delle AI. Dobbiamo imparare a convivere con queste tecnologie preservando la nostra umanità e capacità di pensiero critico. La velocità richiesta dal mercato non è sempre sostenibile, e talvolta è preferibile rallentare per garantire la qualità del lavoro.

Tuttavia, questa scelta ci espone al rischio di essere percepiti come l'anello debole della catena produttiva, l'elemento che impedisce la compressione temporale e l'ottenimento di risultati immediati. Di fronte a questa prospettiva, dovremo interrogarci sulla necessità e utilità del nostro ruolo, o se siamo diventati un peso per l'organizzazione.

Concludo con una riflessione di Stanisław Jerzy Lec che ritengo particolarmente significativa:

```text
"L'anello più debole della catena è anche il più forte perché può romperla."
```

Il programmatore, pur potendo essere considerato l'anello debole del processo di automazione, possiede anche la chiave per spezzare le catene della complessità e della velocità imposte dal sistema.

La nostra forza risiede nella capacità di adattamento, apprendimento ed evoluzione. Anche se il futuro potrebbe etichettarci come l'anello debole della catena, il nostro compito è trasformare questa apparente debolezza nel punto di forza del nostro lavoro e delle nostre organizzazioni, in caso contrario diventeremo presto obsoleti e sostituibili da macchine sempre più intelligenti e autonome.
