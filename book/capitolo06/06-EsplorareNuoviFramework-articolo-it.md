# L'adozione di nuovi framework potrebbe far fallire il tuo progetto

Nel mondo dello sviluppo software, l'attrazione per le novità è sempre forte. È allettante mettere le mani su un nuovo prodotto, magari il primo a risolvere una serie di problemi che gli altri framework non riescono ad affrontare.

Questi nuovi progetti spesso vantano una comunità piccola ma energica, promettono di accelerare i tempi di sviluppo e presentano innovazioni interessanti rispetto ai concorrenti. Tutto ciò sembra molto promettente, ma è davvero la scelta giusta per un progetto a lungo termine?

Donald Knuth, uno dei padri dell'informatica moderna, commentava il proprio codice in questo modo:

```text
Fate attenzione ai bug nel codice soprastante; ho solo dimostrato che è corretto, non l'ho testato.
```

Se fosse stata scritta da un programmatore junior, questa frase potrebbe sembrare una battuta. Ma detta da Knuth, oltre a essere umoristica, potrebbe anche segnalare che quella parte di codice non era testabile, ma solo sintatticamente corretta.

A volte è molto più semplice dimostrare un concetto, descriverne il funzionamento e documentarlo, rispetto alla sua reale applicazione, che potrebbe coinvolgere una serie di aspetti non considerati dalla dimostrazione.

Questo concetto si può parafrasare così: "Non è detto che un'idea brillante funzioni sempre nella realtà". Pensando a ciò, non posso non considerare il mondo delle blockchain: sulla carta strumenti eccellenti, ma nella pratica spesso criticati per prestazioni e utilizzo delle risorse.

Uscendo dal mondo software, pensiamo a prodotti come Segway che, nonostante fosse un'idea brillante, non ha avuto il successo sperato. O a Google Glass, che nonostante fosse un prodotto innovativo, non è mai decollato.

## E i framework?

I framework e, più in generale, le tecnologie software, soffrono spesso di un hype iniziale che galvanizza i programmatori, distraendoli da una solida analisi della loro efficacia nel lungo termine. I concetti utilizzati in quel nuovo software sono applicabili a tutti i progetti? Sono facilmente integrabili con altre tecnologie? Ci sono solide aziende che investono in quella tecnologia? La comunità è attiva e supporta il prodotto?

I cosiddetti "early adopters" sono spesso attratti dalle novità, ma frequentemente non si rendono conto dei rischi che questa scelta comporta. Se va tutto bene, hanno fatto una scelta fortunata che ha portato al successo il proprio software. Ma se il prodotto scelto non riesce a mantenere le promesse, si ritrovano con un software che non funziona come dovrebbe e che richiede un lavoro di manutenzione e refactoring molto più pesante di quanto previsto.

Per chi sviluppa software da oltre 30 anni, il nome Visual Objects farà suonare qualche campanello: doveva essere il nuovo Clipper e portare milioni di programmatori DOS in ambiente Windows. Un'idea fantastica, ma che non ha funzionato: troppi problemi, troppi bug, troppi limiti. Ai tempi aveva alle spalle un'azienda come Computer Associates, che poteva permettersi di investire milioni di dollari in un prodotto, ma nonostante questo, non è mai decollato.

Ecco perché, quando si tratta di scegliere un framework o una tecnologia per un progetto, è importante considerare non solo le sue caratteristiche tecniche, ma anche la sua sostenibilità a lungo termine.

## L'orizzonte temporale: una dimensione cruciale

Ogni volta che valuto un progetto, cerco di anticiparne il ciclo di vita, o almeno quello che dovrebbe essere, basandomi sull'esperienza e sulle informazioni a mia disposizione. La sfera di cristallo non esiste e il futuro non è prevedibile, ma ci sono segnali che fanno capire se un progetto sarà di breve, media o lunga durata.

Per comprendere quanto un progetto possa durare, è importante considerare vari aspetti:

- **Obiettivi a lungo termine**: Quali sono gli obiettivi del progetto? È un prodotto che risolve un singolo problema o qualcosa di strutturato per durare anni o solo pochi mesi?
- **Stabilità del mercato**: Il mercato in cui il progetto opera è stabile o in rapida evoluzione? L'effervescenza di un mercato può portare a cambiamenti rapidi che richiedono una maggiore flessibilità da parte del progetto.
- **Competizione**: Qual è il livello di competizione nel settore in cui opera il progetto? Lavorare in un'arena dove magari gli altri attori provengono da aziende più grandi e strutturate può richiedere una maggiore attenzione alla qualità e alla sostenibilità del progetto.
- **Tendenze del settore**: Quali sono le tendenze attuali nel settore in cui opera il progetto? Alcuni progetti nascono già vecchi, perché si basano su tecnologie obsolete o su modelli di business superati.
- **Risorse disponibili**: Quali risorse sono disponibili per lo sviluppo e la manutenzione del progetto? Si tratta di progetti "one man show" o ci sono team strutturati dietro?

Questi sono solo alcuni degli indicatori possibili, ma basarsi solo sul nome e su ciò che viene promesso è spesso una sottovalutazione del rischio.

Quando si utilizzano framework o tecnologie giovani, è importante considerare che potrebbero non essere supportati a lungo termine o potrebbero non essere in grado di adattarsi ai cambiamenti del mercato. Questo può portare a costi di manutenzione elevati, a problemi di compatibilità e a una maggiore complessità del codice.

D'altra parte, occorre anche valutare i progetti che si intendono realizzare. Potrebbero essere progetti nati e conclusi nel giro di un fine settimana: in questo caso l'esigenza primaria è la risoluzione del problema. Altri potrebbero dover reggere per pochi mesi per soddisfare un'esigenza specifica. Infine, esistono progetti destinati a durare anni, su cui un'azienda intende costruire la propria base operativa: in queste situazioni la scelta del framework e l'architettura di progetto diventa cruciale e non può essere basata solo sulla moda del momento.

L'orizzonte temporale è una dimensione che ogni architetto del software dovrebbe tenere in considerazione, perché influenza notevolmente le aspettative e le scelte che si possono fare.

Per un progetto "one-shot", si può tranquillamente adottare il framework CIRO, creato da un nomade della Tanzania, utilizzato solo dal suo gruppo di amici, con un unico rilascio fatto alcuni anni fa, se risolve in maniera sbalorditiva un problema cruciale per il progetto. Se invece devo realizzare qualcosa che deve durare oltre la scadenza di un dolce al cucchiaio, forse dovrei moderare la mia aggressività nella scelta dei componenti software da impiegare e basarmi su KPI differenti.

## Il rischio dell'abbandono

Mi è capitato di usare prodotti sia "closed source" che "open source", il cui creatore è scomparso nel nulla, così come si è dissolta la comunità che ne faceva parte. Se ciò accade con prodotti "closed", è sicuramente molto preoccupante, ma non cadete nell'illusione che sia tutto rose e fiori se avviene con prodotti "open". Un conto è utilizzare un prodotto, un altro è svilupparlo e conoscerlo in ogni sua virgola.

La mente di chi progetta una soluzione è solitamente intrappolata tra le righe di codice del prodotto stesso ed è certamente più immersa nelle sue logiche interne rispetto a chi lo usa, che spesso sfrutta solo una parte delle sue potenzialità. Non pensate quindi che "open" significhi "c'è un problema: lo risolvo io", perché non è sempre così.

Linus Torvalds, creatore di Linux, ha un'opinione forte su questo argomento:

```text
Il software è come il sesso: è migliore quando è libero e gratuito.
```

Anche se Torvalds utilizza questa citazione per promuovere il software open source, è importante ricordare che "gratuito" non significa necessariamente "senza costi" e che la libertà di disporre dei sorgenti di un progetto non necessariamente significa poterlo mantenere e farlo evolvere.

## L'importanza dell'analisi periodica

Questo è uno dei motivi per cui dovremmo sempre eseguire un'analisi della vita dei prodotti che adottiamo. Un'analisi da ripetere periodicamente, che tenga conto del contesto attuale, della maturità del progetto e delle sue prospettive future.

Se sui progetti brevi si può ignorare questo aspetto, su quelli che superano gli anni di sviluppo, il problema diventa incombente: o si aggiorna il prodotto e le sue dipendenze, o ci si trova in un vicolo cieco a causa delle innumerevoli intrecciature del proprio codice.

Un'analisi periodica ci permette di valutare se il framework o la tecnologia che stiamo utilizzando è ancora adatto alle nostre esigenze, se è supportato attivamente dalla comunità e se è in grado di adattarsi ai cambiamenti del mercato.

## Il rischio dei servizi non standard

Questo si applica anche a tutti i problemi che possono scaturire dall'adozione di un servizio senza standard, che potrebbe essere ritirato dal mercato o raddoppiare i prezzi da una stagione all'altra.

Jeff Bezos ha una visione interessante su come le aziende dovrebbero approcciarsi alla tecnologia:

```text
Bisogna essere testardi nella visione e flessibili nei dettagli
```

Questa filosofia può essere applicata anche alla scelta dei framework, dei servizi e dello sviluppo software: mentre i dettagli tecnici possono cambiare, i principi di base come la scalabilità, la manutenibilità e l'interoperabilità dovrebbero rimanere costanti.

Per questo motivo, realizzare un software fortemente accoppiato con un framework potrebbe portare a problemi di manutenzione e scalabilità in futuro. Se il framework non è più supportato o non è in grado di adattarsi ai cambiamenti del mercato, potremmo trovarci in una situazione in cui è necessario riscrivere gran parte del codice per adattarlo a una nuova tecnologia.

Ho visto prodotti fare scelte tecniche che, sulla carta, sembravano le migliori, e col tempo accorgersi che l'accoppiamento software che era stato realizzato era talmente forte che cambiare una parte significava dover cambiare tutto il resto. Anche questo problema si può evitare con una corretta analisi e una scelta ponderata dei componenti utilizzati, disaccoppiando utilizzo da implementazione e accettando di dover cambiare una parte del software se necessario.

## Conclusioni

Quando si tratta di soluzioni o framework giovani, il rischio di sprecare tempo e risorse è considerevole. Se amate l'incertezza e la durata del progetto non è un fattore che volete considerare, siete liberi di fare qualsiasi scelta e di costruire un prodotto ricco di domande irrisolte.

In caso di errori, tenete presente che potrebbe essere necessario ricominciare da zero, a meno che il vostro software non sia sufficientemente modulare da permettere la sostituzione di un componente senza dover riscrivere tutto il resto.

La scelta di un framework o di una tecnologia dovrebbe essere guidata non solo dall'entusiasmo per l'innovazione, ma anche da una valutazione ponderata dei rischi e dei benefici a lungo termine. La sostenibilità, la manutenibilità e la scalabilità dovrebbero essere sempre in cima alle nostre priorità quando prendiamo decisioni architetturali.
