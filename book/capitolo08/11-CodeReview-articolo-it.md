# “Vediamo chi c’è l’ha più grosso: facciamo code review”

La revisione del codice è uno dei momenti più delicati e importanti di un progetto software. Qualsiasi progetto software che abbiamo sviluppato o svilupperemo nel tempo è stato o sarà sottoposto a una revisione del codice.

Non è immaginabile un codice scritto da chiunque non subisca mutazioni nel tempo. Anche se può valere per singole parti di un progetto, se guardiamo l'interezza di un progetto software, la code review diventa un passaggio significativo fra rimanere piccoli e giocare con le bambole, o uscire allo scoperto e diventare uomini.

Questo passaggio è quindi fondamentale per garantire la qualità del codice, per evitare che errori possano compromettere il funzionamento del software e per allargare la conoscenza del codice a tutto il team. Sì, perché far evolvere il team è un aspetto più importante che sublimare il proprio ego nel guardare una decina di righe che solo chi le ha scritte può capire.

## La code review da fastidio

Esiste però un problema di fondo: ai programmatori la code review infastidisce, non piace, viene ritenuta superflua o sbagliata se fatta da altri e deve essere fatta e decisa solo da loro.  
Per alcuni poi è come perdere un figlio:

```text
Quel codice era scritto in quel modo per una ragione ben precisa: Mario non voleva che nessuno ci mettesse le mani, ma ora che si è licenziato non si capisce più nulla.
```

Un buon momento per fare code review è quando si corregge un bug. Occorre però scardinare l'approccio che viene spesso sposato dai programmatori, che tendono ad essere chirurgici e a risolvere la singola segnalazione, senza sfruttare il pensiero olistico.

```text
Mi hanno segnalato che cliccando su un pulsante c'è un errore, faccio in modo che non ci sia.
```

In realtà, il problema potrebbe essere molto più profondo e richiedere una riflessione più ampia. Ci dovremmo porre il problema di come mai quel pulsante è stato cliccato, se è stato cliccato da un utente, se è stato cliccato da un utente che non avrebbe dovuto cliccarlo, se è stato cliccato da un utente che non avrebbe dovuto cliccarlo in quel momento, se è stato cliccato da un utente che non avrebbe dovuto cliccarlo in quel momento e in quel contesto.

Volendo allargare il pensiero, potremmo anche chiederci se il problema non è esteso ad altri pulsanti, se e come viene segnalato, se ha senso avere quel pulsante o quei pulsanti che fanno quell'operazione, se l'operazione che fa quel pulsante è necessaria, se l'operazione che fa quel pulsante è necessaria in quel contesto.

Allargare il contesto però vuol dire spendere tempo, impiegare risorse, mettere in discussione il proprio lavoro e quello degli altri, vuol dire mettere in discussione il proprio ego e quello degli altri, ma così facendo si migliora il codice, si migliora il sistema, si migliora il team.

Occorre quindi non guardare la singola segnalazione che ci viene fatta, ma cercare di capire il contesto in cui è stata fatta e se ci sono altre parti di codice che potrebbero essere migliorate.

Il pensiero olistico, anche nel codice, è importante: se non capiamo che una singola modifica ha un impatto su tutto il sistema, non possiamo capire il sistema, se non capiamo il sistema, non possiamo migliorarlo.

Come diceva Platone:

```text
Il refactoring è l'arte di togliere il male e aggiungere il bene al codice.
```

Forse l'autore non era Platone, ma il concetto è chiaro: il codice va migliorato, va reso più leggibile, più mantenibile, più testabile.

## Il codice non usato

Se avete lavorato sullo stesso progetto per più di un lustro, la frase:

```text
Quel codice lo abbiamo scritto per "Cliente importante", che non è più nostro cliente, ma non lo togliamo perché "potrebbe" servire
```

è quasi un mantra che sono sicuro avete sentito almeno una volta.  
Stratificare pensieri di questo genere nel corso del tempo porta ad avere un codice che non si capisce, che non si sa cosa faccia, che non si sa perché lo fa e che non si sa come lo fa: le specifiche erano intrecciate con i bisogni del cliente, con le esigenze del team, con le scelte tecniche del momento.

Nel frattempo, il codice è cambiato, il team è cambiato, il cliente è cambiato, le esigenze sono cambiate, le scelte tecniche sono cambiate: è giusto che il codice cambi o venga rimosso dal progetto. Mantenere codice non usato è costoso e col tempo rappresenta un inutile debito tecnico.

Ci sono aziende che hanno capito quanto sia costoso e inutile mantenere progetti che non vengono più usati: il codice è un costo, non un valore, se non viene usato.

Google, ad esempio, ha una ricca storia di progetti che sono stati abbandonati. Ne potete trovare traccia su Wikipedia:

```text
https://en.wikipedia.org/wiki/Category:Discontinued_Google_services
```

## Io uso i TAB, chi usa gli spazi non è un programmatore bravo

In una puntata di "Silicon Valley", il protagonista Richard scopre che la sua fidanzata Winnie utilizza gli spazi al posto dei TAB per indentare il codice e la lascia: è un'esagerazione cinematografica, ma conosco persone che non accetterebbero mai di lavorare con qualcuno che usa gli spazi al posto dei TAB e viceversa.

Scardinare questa abitudine, e lo dice uno che usa gli spazi da quando ha appoggiato l'indice sulla tastiera, è difficile, ma necessario: il codice deve essere uniforme, deve essere coerente, deve essere leggibile. Avere stili diversi all'interno del team è controproducente, rallenta il lavoro, aumenta la possibilità di errori, rende difficile la manutenzione.

All'interno di una code review è necessario discutere anche di queste cose: non si tratta di imporre un proprio stile, ma di trovare un compromesso che possa essere accettato da tutti e possibilmente non sia un peso per nessuno.

Una volta raggiunto un accordo, è importante rispettarlo: se si decide di usare gli spazi al posto dei TAB, non si può tornare indietro.

Si tratta però di qualcosa difficile da accettare e da mettere in campo, sia perché alcuni programmatori considerano il codice come un figlio, che non si può cambiare, sia per il fatto che, anche imponendo uno stile uniforme, prima o poi qualcuno non capirà la specifica, altri configureranno l'IDE in modo sbagliato o perderanno le impostazioni al primo aggiornamento.

In queste situazioni, dove non è il linguaggio stesso che ci aiuta a mantenere uno stile uniforme (sì, ci sono linguaggi che lo fanno per noi in modo assolutamente dittatoriale), è importante utilizzare degli strumenti che ci permettano di automatizzare il più possibile la formattazione del codice.

All'interno di uno dei progetti più grossi che seguo, è stato deciso di adottare OpenRewrite, uno strumento che riformatta il codice in modo automatico, uniforme e coerente, riducendo le differenze fra diversi stili di programmazione: uniformare, oltre a rendere il codice più coerente, velocizza l'inserimento di nuovi membri nel team e il passaggio di un componente da un team all'altro.

## Resistenza al cambiamento

Anche se la maggior parte dei programmatori è d'accordo sulla necessità di una code review, spesso si rifiutano di accettare i cambiamenti proposti, un po' per pigrizia, un po' per orgoglio, un po' per abitudine.

Se lavori da anni nello stesso modo, e funziona, perché cambiare?

```text
Il mio codice nasce perfetto
```

Purtroppo no: non è così. All'interno di un team, l'aspetto che deve prevalere è la lettura del codice da parte di tutti, deve prevalere la facilità di inserimento di una nuova risorsa, deve prevalere la semplicità di modifica anche dopo mesi che non si mette mano ad alcune righe.

Non importa quindi se l'IDE che usi formatta il codice in un certo modo, non importa se ti è sempre piaciuto dichiarare le variabili con "_", aderire ad uno standard diffuso, spontaneamente o tramite delle automazioni, è un vantaggio, anche se in prima battuta può sembrare un peso.

## Clean Code

Uno degli obiettivi che dovrebbe avere una code review è quello di scrivere codice pulito, leggibile e mantenibile.

A volte mi sono trovato di fronte alla scelta se mantenere del codice che funzionava, o smontarlo perché, pur superando in modo eccellente qualsiasi test funzionale, era scritto in modo oscuro, difficile da leggere e da mantenere, e ogni volta che mettevo una persona davanti a quel codice, la sua espressione era sempre la stessa:

```text
Non capisco cosa fa
```

A volte crediamo che usare l'ultima sintassi proposta da un linguaggio sia la soluzione a tutti i nostri problemi, ma non sempre è così. A volte i nuovi costrutti si basano su concetti difficili da comprendere e da spiegare, a volte sono solo zuccherini per farci sentire più bravi: "sugar code" come lo chiamano alcuni.

Non sempre il codice più compatto e coinciso è il migliore: a volte è meglio scrivere 10 righe di codice che fanno quello che devono in modo chiaro e leggibile, piuttosto che una sola riga che fa la stessa cosa, ma che nessuno capisce, per guadagnare nulla a livello prestazionale e funzionale.

## Automatizzare il possibile

Stranamente, i programmatori accettano di buon grado qualcosa che viene proposto da un programma, rispetto a quanto viene proposto da qualcuno all'interno del team.

Se anche nel vostro team c'è lo stesso clima, potete proporre l'introduzione, all'interno della pipeline di progetto (sperando ne abbiate una), di processi di normalizzazione di codice e analisi statica.

I primi serviranno a diminuire la differenza di stile fra un programmatore e l'altro, gli altri serviranno a suggerire modifiche, a farci capire dove sono nascosti bug, dove mancano dei test, dove la complessità cognitiva è troppo alta o dove possiamo ridurre il codice, senza perdere di chiarezza o efficacia.

## Ma a me non interessa

Ogni tanto passo il mio tempo libero a studiare progetti di altri programmatori, faccio girare qualche analizzatore e provo a correggere un po' di codice: è un buon allenamento e mi permette di vedere come altri affrontano i problemi o sottovalutano le conseguenze del loro codice.

Durante queste scorribande, mi sono imbattuto in approcci completamente differenti da parte di singoli programmatori o team di programmatori ai quali ponevo le mie Pull Request.

Fra tutti i progetti che ho analizzato, vorrei parlare di due che mi hanno particolarmente colpito per come il team ha gestito il mio contributo.

La prima Pull Request riguarda il JDK di OpenJDK. Mi sono accorto che, per distrazione, 82 sorgenti contenevano dei doppi ";" alla fine di una riga.  
Capite che non si tratta di qualcosa di importante, possiamo anche dire che si tratta di qualcosa di trascurabile, ma ho deciso di fare una Pull Request per correggere il problema e capire come si sarebbe comportato il team di sviluppo.

Potete trovare la PR a questo indirizzo:

```text
https://github.com/openjdk/jdk/commit/ccad39237ab860c5c5579537f740177e3f1adcc9
```

L'approccio, a mio avviso, è stato interessante: prima di tutto sono stati coinvolti nell'analisi della modifica 8 persone, essendo le modifiche orizzontali a tanti package di Java.  
Dopo una discussione orizzontale di vari maintainer e aver constatato che il problema era reale, è stata aperta una issue:

```text
https://bugs.openjdk.org/browse/JDK-8282657
```

Si è anche discusso di una possibile modifica ai tool di build, che già rimuovevano gli spazi a fine riga, introducendo la rimozione dei doppi caratteri ";".

Questo approccio denota un team che analizza ogni singola modifica, che discute e che cerca di capire se la modifica proposta è effettivamente utile o se è solo un capriccio di qualcuno.  
In questo caso, hanno capito che si trattava di una modifica banale, ma orientata alla pulizia del codice, e per questo è stata accettata.

Un secondo caso invece coinvolge un tool di sicurezza realizzato da un singolo maintainer, messo anch'esso su GitHub.  
In quel caso, avevo proposto una PR molto più seria. Era presente del codice ridondante, venivano utilizzate classi sincronizzate in processi nei quali non serviva una sincronizzazione, alcune risorse erano aperte senza una chiusura esplicita e così via.

Si trattava quindi di una modifica orientata a migliorare la qualità del codice e a ridurre la possibilità di errori, non qualcosa di banale come la rimozione di un carattere.  
Oltre a questo, il passaggio a oggetti non sincronizzati portava a un aumento prestazionale nell'intorno del 20%: tutto questo senza snaturare il codice, ma solo utilizzando i giusti costrutti e, a parità di interfacce, le giuste classi.

In questo caso, ero convinto che non ci fossero problemi a inserire questo codice nel progetto, ma la risposta è stata negativa.  
Il maintainer ha risposto che non intendeva integrare nel suo codice i suggerimenti che derivavano da un analizzatore sintattico e che potevo usarli sul mio fork e lui non li avrebbe mai integrati.

```text
Se non ti piace il mio codice, fai il tuo fork e modificalo come vuoi
```

Questa è la classica risposta di chi non vuole cambiare, di chi non vuole accettare che il suo codice possa essere migliorato, di chi non vuole accettare che il suo codice possa essere cambiato da altri, nonostante le modifiche possano migliorare la leggibilità e portino a tangibili miglioramenti.

## Conclusione

Anche quando tutto funziona, revisionare il codice è importante: permette di migliorare il progetto, di migliorare il team e tagliare quelli che sono i debiti tecnici.

Diminuire il debito tecnico, avere il coraggio di smontare anche codice funzionante, buttare codice non più usato, dare ascolto a revisori statici, uniformare lo stile di programmazione, automatizzare il più possibile la formattazione del codice, sono tutti passaggi che possono migliorare il codice e il team.

Non abbiate paura di mettere in discussione quello che è stato scritto in passato e allargate la visione quando dovete mettere le mani al codice: non guardate solo la singola modifica, ma cercate di capire il contesto in cui è stata fatta e se ci sono altre parti di codice che potrebbero essere migliorate.

Un prodotto migliore passa attraverso tanti piccoli passi e non è detto che, pur avendo centinaia di test funzionanti, il codice sia perfetto: la code review è un passaggio fondamentale per garantire la qualità del codice e per evitare che errori possano compromettere il funzionamento del software.
