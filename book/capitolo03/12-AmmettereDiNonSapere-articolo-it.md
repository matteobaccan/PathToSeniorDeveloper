# La forza di ammettere di non sapere

Il mondo della programmazione è un universo in continua evoluzione, dove le competenze tecniche rappresentano solo il punto di partenza.

Tutti guardano con timore il mondo delle AI, sulla carta software in grado di conoscere più di qualsiasi programmatore e capaci di generare codice con la facilità di bere un sorso d'acqua, ma la differenza tra un buon programmatore e un grande programmatore non risiede solo nella capacità di scrivere righe di codice, ma anche nell'abilità di interpretare correttamente le specifiche, di vedere oltre quanto viene richiesto, di riconoscere quando una strada è sbagliata e sarebbe opportuno intraprenderne un'altra.

Tutte queste capacità si acquisiscono con l'esperienza e al momento non esistono AI con tali caratteristiche.

Se ti definisci programmatore, ma hai comunque paura: è normale.

La paura di non sapere abbastanza, di essere superato da un software è un'ombra che accompagna costantemente il percorso professionale di ciascun programmatore.

Se hai appena capito la differenza tra un `for` e un `while` e ti scende una goccia di sudore quando vedi una shell: è perfettamente normale. Sei un junior e ti spaventi per cose che un giorno imparerai a fare con gli occhi chiusi.

Ma questa paura grava anche sulle spalle di chi lavora da anni, che ha scritto più cicli for che il proprio cognome, che identifica i bug solo guardando il codice e che possiede una visione olistica dei progetti.

## La paura di non sapere

La paura di non sapere è una costante di questo lavoro che deve essere presto accettata e superata, poiché ci blocca, impedendoci di crescere e migliorare.

Per fare il programmatore servono competenze, e più se ne acquisiscono, più ci si rende conto che ce ne sono sempre di nuove da apprendere. Allo stesso tempo non è possibile fermarsi, limitarsi a una nicchia o specializzarsi in un singolo ambito, perché ci sarà sempre qualche sviluppatore che, magari lavorando dalla sua capanna in cima a un albero, creerà codice destinato a diventare fondamentale per il tuo lavoro.

Non possiamo conoscere a pieno tutti i prodotti che utilizziamo né tutto ciò che viene rilasciato ogni giorno: o dedichiamo tempo a capire cosa succede o passiamo le giornate a scrivere codice. Ma anche se fossimo in grado di fare entrambe le cose, non saremmo comunque in grado di conoscere tutto.

Chi sa tutto? Le AI? No, nemmeno loro. Apprendono quanto riescono ad assimilare dalla rete, ma se il dato non è presente o viene interpretato male, il risultato sarà errato: esiste un mondo di codice in ambito legacy, privo di documentazione che le AI non conoscono. Ci sono tutti i prodotti closed source che non possono essere analizzati, tutti quelli che devono ancora essere rilasciati e così via.

Quindi mettiamoci l'anima in pace: non possiamo sapere tutto e anche con gli strumenti più moderni non saremo mai in grado di conoscere ogni cosa. Ci saranno sempre gradi di ignoranza o di errore in tutto il codice che andremo a scrivere.

Allo stesso modo, tutto quello che scriviamo oggi potrebbe rivelarsi sbagliato: perché non conosciamo a pieno un prodotto e perché la tecnologia evolve e cambia, e ciò che oggi è considerato corretto, domani potrebbe essere ritenuto errato.

## Ero ignorante e non lo sapevo

Ultimamente ho lavorato sull'ottimizzazione di un prodotto Java al quale veniva chiesto di eseguire una serie di operazioni entro la soglia di 10 millisecondi.

Il codice sembrava corretto, ma saltuariamente il programma superava i 100 millisecondi.
In un ambiente dove anche i millisecondi avevano un peso, questa oscillazione non era tollerata perché superava lo SLA del servizio che dovevamo fornire.

Qual era il problema? L'istanziazione di un oggetto richiamava il classloader per cercare una certa tipologia di classe, invece di istanziare in modo diretto una classe. Questa operazione, che nel 99,999% dei casi si risolveva in meno di 1 millisecondo, in alcuni casi arrivava a 100 millisecondi.

La soluzione? Abbiamo evitato la ricerca della classe in modo dinamico, passando a un'istanziazione statica.
Peso della modifica: 1 riga di codice, ma il ritardo saltuario era sparito.

Non conoscevamo così in profondità la classe che usavamo, e in condizioni normali il problema non sussisteva: appariva solamente in momenti di stress applicativo in forte concorrenza.

Come l'abbiamo capito? Parlandoci fra di noi, confrontandoci, mettendo insieme le nostre competenze ed esperienze.

## L'ignoranza è una risorsa

In questo mare di conoscenza – o di ignoranza, se si vuole vedere il bicchiere mezzo vuoto – l'unica cosa che possiamo fare è potenziare quelle che sono le soft skill, un tempo sottovalutate e oggi più che mai essenziali.

Sia ben chiaro: le competenze tecniche sono fondamentali, così come è essenziale conoscere e usare bene i nuovi strumenti che ci vengono messi a disposizione ogni giorno, ma per chi ha trascorso anni a lavorare con il codice, ci sono delle skill che fanno la differenza quando si collabora in team.

Assodato che libri, manuali e AI non avranno mai tutte le risposte, la cosa che apprezzo maggiormente è il **coraggio di chiedere**.

Ci sono competenze ed esperienze che risiedono solo all'interno delle persone, e spesso è più facile chiedere a chi sa piuttosto che cercare di capire da soli.

Per paura di essere umiliati o derisi, non osiamo fare una domanda a un collega, non diciamo "non ho capito", non abbiamo il coraggio di chiedere chiarimenti. Passiamo ore davanti a pezzi di codice incomprensibili, chiediamo aiuto in forma anonima su forum, Reddit, Stack Overflow o a varie AI, ma piuttosto che rivolgere una semplice domanda al collega seduto accanto a noi, preferiremmo quasi darci fuoco.
Non facciamo gruppo e preferiamo spaccarci la testa da soli di fronte a un problema.

L'orgoglio si trasforma in una catena invisibile che ci limita, ci paralizza, ci fa sprecare tempo prezioso e ci induce a commettere errori evitabili.

Temiamo di essere giudicati come deboli, ma in realtà, ammettere di non sapere è una grande virtù.  

Una volta un antico filosofo disse:

```text
Il tuo mantra per la vita deve essere "dignità zero"
```

In realtà non era un filosofo, ma Mauro Repetto, fondatore degli 883, ma il messaggio che arriva è lo stesso: **seguire i propri sogni senza preoccuparsi delle critiche o del giudizio altrui**.

Molte volte è infatti la paura del giudizio che ci ferma e non ci permette di crescere. Ma se non chiediamo, come possiamo imparare? Se non ammettiamo di non sapere, come possiamo migliorare?

## Gestione dell'ignoranza

Siamo tutti ignoranti, ma in argomenti diversi. Ammettere di non sapere e palesare questo aspetto in azienda a volte può far muovere delle risorse.

Anni fa mi trovavo in un'azienda dove avevamo deciso di puntare su C++ per il nuovo prodotto che volevamo realizzare: i motivi erano la velocità di esecuzione e la possibilità di scrivere codice più vicino all'hardware.
Col tempo la scelta si è rivelata sbagliata, non per i presupposti iniziali, ma per il fatto che si rivolgeva a un bacino di programmatori che non avevano mai lavorato con quel linguaggio e provenivano da linguaggi più semplici.

In quel frangente il management si accorse di una lacuna: il team nel quale ero inserito e che doveva sviluppare in C++ non aveva, o aveva solo in parte, adeguate competenze per poter realizzare il prodotto che ci eravamo prefissati.
Per questo motivo venne organizzato un corso con un esperto del linguaggio, per sbloccarci su tutta una serie di aspetti che non avevamo considerato e non conoscevamo.

Palesare la nostra ignoranza ci fece fare un salto in avanti, ci permise di capire dove stavamo sbagliando e di correggere il tiro, ma soprattutto ci fece comprendere che non siamo soli e che chiedere aiuto è normale.

Se questo vale per un team, dove forse è anche più facile chiedere, vale molto anche per i singoli.

## Il coraggio di chiedere

Anni fa lavoravo per un'azienda che aveva assunto diversi ragazzi freschi di diploma. Le loro competenze erano variegate: alcuni dimostravano già un certo talento, altri meno. Tuttavia, uno in particolare si distingueva dagli altri non per le sue capacità tecniche – anzi, aveva notevoli lacune – ma per la sua straordinaria predisposizione a chiedere chiarimenti, anche ripetutamente durante la giornata. Questo atteggiamento, apparentemente semplice ma in realtà rivoluzionario, con il passare del tempo lo ha portato a superare tutti i suoi coetanei.

Il suo ChatGPT erano i colleghi, le persone più esperte di lui, che lo indirizzavano, gli spiegavano cosa occorreva fare e non fare e dove doveva migliorare il proprio studio.

La paura di fare brutte figure è spesso una gabbia che ci tiene intrappolati nella nostra comfort zone. Abbiamo una scelta: rimanere prigionieri della paura o liberarci con il coraggio di chiedere. La strada per diventare programmatori migliori inizia da qui.

## Il mito del tuttologo

Il mondo tech abbonda di persone che si ergono a tuttologi, convinte di sapere tutto e di non aver bisogno di alcun aiuto esterno. Questa pericolosa illusione nasce da un'immagine distorta della perfezione.
Considerate i supereroi come metafora: vengono rappresentati come esseri perfetti, infallibili, autosufficienti e impavidi. Ma noi non siamo supereroi con superpoteri: siamo esseri umani, con tutti i nostri limiti e le nostre fragilità.

Provate a guardare anche tutte le persone che seguite sui social. Spesso partono da argomenti che conoscono, sono molto spigliate nel farlo e grazie a questo attirano follower.
Col tempo, in modo più o meno inevitabile, la vena creativa diminuisce e la ricerca spasmodica di argomenti interessanti porta a parlare di cose che non si conoscono bene, ma che si pensa possano interessare.

A questo punto la qualità si deteriora, ma visto che il pubblico continua ad apprezzare e i follower aumentano, si persevera su questa strada, fino a quando non ci si ritrova a parlare di argomenti che non si conoscono affatto.

Questo è il momento in cui si diventa tuttologi, si crede di poter parlare di tutto e di sapere tutto, ma in realtà si è solo un bluff.

Questa situazione capita più o meno a tutti col tempo, ma è importante riconoscerlo e non cadere nella trappola del tuttologo.

Se il tuo seguito ti vede come una guida, come un punto di riferimento, è importante a un certo punto fermarsi, capire il proprio limite, ammettere di non sapere e far intervenire chi è esperto di un certo argomento.

La differenza fra un tuttologo e un esperto è tutta qui: se siamo esperti e vogliamo il meglio per un certo argomento, andremo a chiedere a chi, su un particolare tema è più ferrato di noi e saprà meglio indirizzarci, e non sempre si tratta di una AI, ma di una persona fisica, con un nome e cognome.

## Chiedere da solo però non basta

Abbiamo trovato il coraggio di chiedere? Di far intervenire l'esperto? A questo punto potrebbe nascere un secondo problema: fingere di capire.

Già chiedere è un grande passo, ma ammettere di non aver capito una risposta è un secondo passo che spesso non si fa. Si preferisce fare finta di aver compreso, anche se non è così, per paura di essere giudicati come stupidi.

```text
Repeat and rephrase
```

Un modo semplice per verificare la comprensione di un concetto è ripeterlo e riformularlo con le proprie parole. Se non si riesce a farlo, significa che non si è capito bene e occorre chiedere ulteriori chiarimenti.

## La differenza fra prosciutto cotto e prosciutto crudo

Io non riesco a distinguere il prosciutto cotto dal prosciutto crudo, è qualcosa che mi porto avanti da un sacco di anni. Il mio cervello si rifiuta di associare la parola al prodotto. So cosa voglio, ma non riesco ad associare la giusta parola.

```text
Passami il prosciutto cotto
```

è una delle domande più imbarazzanti che mi possano fare, perché so che la risposta sarà:

```text
Quello è il prosciutto crudo
```

Col tempo ho capito il problema: associavo al colore scuro la cottura e al colore chiaro la non cottura dell'alimento. Il mio cervello associava al contrario le parole, e invertivo il risultato, sapendo che c'era qualcosa che non andava, ma non riuscendo a capire cosa.

A furia di sbagliare ho iniziato a chiedere, e dopo tante spiegazioni, tanti modi per ricordare, ho capito come distinguere il prosciutto cotto dal prosciutto crudo: ma se non avessi iniziato a chiedere, forse non avrei mai avuto un meccanismo in testa in grado di farmi capire la differenza.

## La paura del giudizio

Essere giudicati, essere visti come quello che non sa, è una paura che ci blocca e ci impedisce di crescere. Ma se non chiediamo, come possiamo imparare?

Allo stesso modo, se superiamo questa paura nella domanda, dobbiamo superarla anche nella risposta: non basta chiedere, occorre anche capire la risposta e ammettere di non comprendere.
Chiedere senza capire equivale a non chiedere, ma anche ammettere di non aver compreso la risposta è un'arte che deve essere appresa col tempo.

## Fail-forward culture

Un altro concetto che mi affascina è quello della fail-forward culture, ovvero la cultura del fallimento. Fallire è normale, è umano, è un passo necessario per crescere e migliorare.

Ammettere di non sapere, sbagliare e usare il fallimento come trampolino di lancio per migliorare è una delle chiavi per diventare un programmatore migliore.

Purtroppo non sapere, fallire, mostrarsi vulnerabili viene ancora percepito come un difetto: in realtà rappresenta un potente strumento per crescere, imparare e migliorare, una lezione che dovrebbe essere trasmessa fin dall'infanzia.

```text
Non trattenerti per paura di sbagliare, ma sbaglia per imparare
```

## Conclusioni

La prossima volta che esitate a fare una domanda, chiedetevi: preferisco apparire momentaneamente insicuro o rimanere bloccato per sempre?

E se qualcuno dovesse deridervi per le vostre domande apparentemente ingenue, ricordate che è proprio lui, non facendole, a limitarsi e a costruire lentamente una gabbia invisibile dalla quale sarà sempre più difficile uscire.

Nessuno nasce sapendo tutto, ma solo chi ha il coraggio di ammettere di non sapere può veramente imparare e crescere.
