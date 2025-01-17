# "Puoi cambiare questa condizione nel codice? Cosa ci vuole?"

Cosa differenzia un programmatore senior da un programmatore junior? La capacità di valutare le conseguenze di una modifica al codice diranno in molti, in realtà è la perdita di spensieratezza e un insieme di paure regresse.

## La paura dei senior

Un tempo ero molto più veloce nel cambiare un algoritmo, nella modifica di un parametro di una funzione, nella creazione o distruzione di flussi e così via. L'obiettivo era, prima di tutto, fare quello che chiedeva il cliente e solo in seconda battuta fare in modo che il codice fosse mantenibile o che la scelta presa fosse la migliore all'interno di una serie di scelte più o meno ponderate.

Poi sono invecchiato e ho iniziato ad usare i test per capire se il mio codice andasse bene anche dopo una modifica, ho iniziato a scrivere documentazione per capire perché avevo ragionato in un certo modo e ho iniziato a fare code review per migliorare la comprensione del codice e la sua manutenzione.

Questo nuovo approccio "complicato" il mio lavoro, o per meglio dire: ha allungato i processi che, da una richiesta, portavano alla soluzione finale.
Una modifica che un tempo facevo in 10 minuti, ora occupa una giornata intera, perché devo valutare tutti gli impatti che quella modifica può avere, far girare tutti i test automatizzati, eseguire qualche test manuale dove non sono riuscito ad automatizzare, scrivere la documentazione, effettuare il merge con il codice principale, aspettare il build e i test di integrazione, verificare che tutto funzioni e finalmente dichiarare l'issue risolta, sperando di non aver dimenticato qualcosa.

Gli anni passano ed è inevitabile che ci sia l'evoluzione dal bambino spensierato che effettua una push senza test, alla cariatide che aggiusta anche gli spazi quando deve aggiungere codice al branch main (no, "master" non si utilizza più).

```text
Quello che una volta era un "sì" felice ed entusiasta, 
cresce in un "sì, ma faccio anche questo", 
piano piano diventa un "ni", 
fino ad arrivare ad un "no"
o peggio ancora un "dipende".
```

## I senior non sono cattivi

Non è per cattiveria che succede tutto questo, è per la consapevolezza di quanto gira attorno a una singola riga di codice. La consapevolezza dell'errore o degli impatti di una modifica e per uno sterminato regresso che troppe volte ha minato la certezza che una singola condizione possa essere cambiata senza problemi.
Questo non vuol dire che le modifiche non vanno fatte, vuol solo dire che vanno sempre valutati gli impatti, in modo da non creare problemi più grandi di quelli che si vogliono risolvere e che spesso, più si invecchia e più gli impatti si moltiplicano nella testa del programmatore.

Pensiamo al ciclo di vita di un software e alla sua progettazione. All'inizio sviluppare un prodotto è relativamente facile: vediamo il nostro obiettivo, abbiamo un'idea su come raggiungerlo, facciamo in modo che clienti e stakeholder (ogni tanto mettere un inglesismo a caso aiuta a far sembrare un ragionamento intelligente) siano soddisfatti, e se abbiamo fortuna riusciamo a creare un team coeso sul prodotto sia dal punto di vista tecnico che umano. Questo non è sempre scontato perché a volte basta un singolo elemento fuori dal coro in grado di destabilizzare un intero gruppo. Una volta raggiunto questo obiettivo, quando occorre fare una modifica tutti i membri sono allineati e consapevoli di quello che serve realizzare.

Quando si esce da questa fase di euforia collettiva e si esce dalla fase creativa, il team di sviluppo inizia a cambiare rispetto alla sua forma originale. Contestualmente il cliente diminuisce il budget, perché si entra in una fase di manutenzione e se non si presta la dovuta attenzione si inizia a perdere la padronanza del prodotto.

```text
No, non sono certamente i test che possono governare il prodotto,
ma sono le teste che lo hanno ideato.
```

Il turnover di progetto è un processo inevitabile, a meno che non vi troviate in un igloo in mezzo al polo, privi di connessione internet, e i poveri programmatori che hanno realizzato il progetto non siano in grado di inviare un curriculum se non attaccandolo ad una foca (anche se esiste sempre la possibilità che il programmatore si dedichi alla pesca, sua grande passione sopita dal codice).

Quando si cambia un componente del team, si perde una parte di conoscenza del prodotto e si inizia a perderne la padronanza. A cascata ogni intervento diventa sempre più costoso, lungo e rischioso.

## La manutenzione di un progetto cambia le regole?

In un normale ciclo di vita di un prodotto succede che alcune parti siano soggette ad aggiornamenti frequenti, ma molte altre parti, per un discorso di maturazione, carenza di richieste o stabilità, non abbiano necessità di modifiche. Rendere rarefatte le modifiche diminuisce la conoscenza del codice da parte del programmatore stesso che le ha realizzate. Questo comporta che la persona che ha scritto 2 anni prima quelle righe di codice è normale che non le ricordi e abbia necessità di riguardarle per ricordare i processi che ne avevano portato la realizzazione.

Più è verticale la modifica, più è poi difficile ricordarne la ragione: non ricordi perché all'interno di una connessione ad una risorsa esterna hai messo un parametro e non un altro, perché usi una suite di cifratura al posto di un'altra o magari hai un branch aperto da mesi, in attesa di una verifica con un cliente su una funzionalità urgente, che è diventata all'improvviso di scarsa importanza, ma ora occorre fare il merge in una baseline con 400 push in più e ti chiedi se ha più senso rifare tutto da capo o applicare le modifiche a un rebase.

In mezzo a questo tipo di interventi ci sono i lavori di tutti i giorni, le modifiche alle funzionalità, le correzioni di bug, le richieste di nuove funzionalità, le correzioni di nuovi bug che hai introdotto correggendo un bug, il codice che ha introdotto un collega con scarsa conoscenza del prodotto, i cambi di comportamento introdotti dall'uso di un aggiornamento o un nuovo componente che obbliga un cambio di codice e introduce un'anomalia indiretta.

Tu che hai scritto quel codice non lo ricordi, capisci che a fronte di una serie di cambiamenti la modifica da fare è più grande di quanto prospettato, ma devi capire come farla, perché hai un ricordo dei razionali per i quali è stato fatto il codice precedente e capisci che non è una modifica banale. Figuriamoci chi deve sistemare lo stesso codice ed è la prima volta che mette le mani su quella parte di programma.

Come diceva Eraclito:

```text
Nessun uomo può attraversare lo stesso fiume due volte,
perché né l'uomo né il fiume sono più gli stessi
```

Questa frase può essere facilmente riapplicata al codice: ogni modifica, anche la più piccola, cambia il codice e il contesto in cui si trova, che è diverso dal contesto in cui era stato realizzato e anche la persona è differente rispetto alla persona che aveva scritto quel codice.

## Caso d'uso di una nota Banca italiana

Per un attimo immaginate di essere un programmatore senior di una "banca qualsiasi", dove vi è stato detto che si doveva procedere ad un aggiornamento di sistema e relativo firmware, che non avrebbe portato a nessun danno e che si sarebbe proceduto a fare l'aggiornamento in produzione.
Avendo visto questo tipo di interventi più volte nella vostra vita, la prima cosa che vi viene in mente di fare è quella di eseguire un test, ma non esiste un ambiente di test che copra esattamente la dimensione della produzione, sia per dimensionamento che per casi d'uso. Sconsigliate l'aggiornamento massivo, ma il produttore della soluzione assicura che non ci saranno problemi, il reparto di sicurezza vi avvisa che occorre mettere l'aggiornamento entro una certa data perché altrimenti non si è conformi alle regole aziendali e che comunque in caso di problemi si può tornare indietro.

Vostro malgrado accettate, spinti anche dal fatto che "lavoriamo con la metodologia agile e dobbiamo essere pronti al cambiamento" e che "non possiamo essere sempre negativi".

```text
Le interruzioni agli accessi ai servizi online (come app, app Invest, Internet Banking e Smart Business)
si sono verificate in seguito all'installazione di un aggiornamento del sistema operativo
e del relativo firmware che ha comportato una situazione di instabilità. 
Ci teniamo ancora a scusarci e riteniamo fondamentale ringraziarti ancora per la comprensione dimostrata.
```

Un "banale" aggiornamento di sistema operativo e firmware ha comportato una situazione di instabilità per ben 5 giorni.

Chiaramente, in questo caso ipotetico, il problema non è stato l'aggiornamento, ma la mancanza di test, la mancanza di un ambiente di test che coprisse la produzione, la mancanza di un rollback immediato e la mancanza di un piano di disaster recovery o la sottovalutazione del rischio.

## Qual è la percezione della modifica all'esterno del progetto?

Spesso chi è fuori dal progetto ha una percezione completamente diversa dello sviluppo software e spinge per realizzare le modifiche il prima possibile.

```text
Mi serve per ieri
```

Questa frase è un classico, ma spesso non si capisce che una modifica, anche banale, può comportare una serie di problemi che vanno ben oltre la modifica stessa.

```text
Ho chiesto solo di cambiare una condizione, perché Mario mi crea tutti questi problemi?
Ora assegno il compito a Bruno che lo risolve in 2 minuti
```

Ci sono situazioni all'interno dei progetti che permettono di alterare il codice molto velocemente, ed altre situazioni in cui una modifica, anche banale, può richiedere molte riflessioni: anche se si tratta di poche righe di codice o addirittura una sola condizione aggiuntiva.
Ogni programmatore affronta la modifica in modo diverso, in base alla sua esperienza, alla conoscenza del prodotto e alla conoscenza del codice. Più abbiamo programmatori esperti del prodotto, più è probabile che la modifica venga valutata attentamente, perché si è consapevoli di quanto una modifica possa comportare. Meno il programmatore è a conoscenza del prodotto, più è probabile che la modifica venga fatta velocemente.

## Conclusioni

Ogni modifica, anche la più banale, può comportare dei problemi prestazionali, di regressione, di sicurezza, di manutenibilità, di comprensione del codice, di documentazione, di test, di deployment.

Allo stesso modo delle alterazioni esterne al progetto possono creare gli stessi problemi: ho aggiornato il sistema operativo, ho aggiornato un driver, ho aggiornato il firmware e ora non funziona più nulla.

La pressione che viene messa addosso ad un programmatore aumenta progressivamente col tempo perché parallelamente aumenta la consapevolezza di tutto quello che può andare storto e di quanto sia difficile risolvere un problema una volta che si è verificato.

Questo può portare a situazioni in cui un programmatore senior si rifiuta di fare una modifica, perché sa che i rischi sono troppo alti, o perché sa che la modifica richiederebbe troppo tempo e risorse per essere fatta correttamente.

La prossima volta che guardate un programmatore, che da molti anni lavora sullo stesso codice e non vuole modificarlo e vi avverte su ogni alterazione interna o esterna al progetto, non pensate a lui come a un incapace, ma piuttosto come a una persona consapevole ed utilizzate il suo consiglio per evitare di far crollare il vostro progetto e soppesare al meglio rischi e benefici di ogni modifica perché infondo, come diceva Isaac Asimov:

```text
Nessuna decisione sensata può essere più compiuta senza tenere
conto non solo del mondo come è ora, ma di come sarà
```
