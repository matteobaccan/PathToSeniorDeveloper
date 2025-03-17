# La fuerza de admitir que no se sabe

El mundo de la programación es un universo en constante evolución, donde las habilidades técnicas representan solo el punto de partida.

Todos miran con temor el mundo de la inteligencia artificial, en teoría software capaz de saber más que cualquier programador y capaz de generar código con la facilidad de beber un sorbo de agua, pero la diferencia entre un buen programador y un gran programador no reside solo en la capacidad de escribir líneas de código, sino también en la habilidad de interpretar correctamente las especificaciones, de ver más allá de lo que se pide, de reconocer cuándo un camino es incorrecto y sería conveniente tomar otro.

Todas estas habilidades se adquieren con la experiencia y, por el momento, no existen inteligencias artificiales con tales características.

Si te defines como programador, pero aún así tienes miedo: es normal.

El miedo de no saber lo suficiente, de ser superado por un software es una sombra que acompaña constantemente el camino profesional de cada programador.

Si acabas de entender la diferencia entre un `for` y un `while` y te cae una gota de sudor cuando ves una terminal: es perfectamente normal. Eres un junior y te asustas por cosas que un día aprenderás a hacer con los ojos cerrados.

Pero este miedo también pesa sobre los hombros de quienes llevan años trabajando, que han escrito más ciclos for que su propio apellido, que identifican los errores solo con mirar el código y que poseen una visión holística de los proyectos.

## El miedo a no saber

El miedo a no saber es una constante de este trabajo que debe ser pronto aceptada y superada, ya que nos bloquea, impidiéndonos crecer y mejorar.

Para ser programador se necesitan habilidades, y cuanto más se adquieren, más se da uno cuenta de que siempre hay nuevas cosas por aprender. Al mismo tiempo, no es posible detenerse, limitarse a un nicho o especializarse en un solo ámbito, porque siempre habrá algún desarrollador que, tal vez trabajando desde su cabaña en la cima de un árbol, creará código destinado a convertirse en fundamental para tu trabajo.

No podemos conocer plenamente todos los productos que utilizamos ni todo lo que se lanza cada día: o dedicamos tiempo a entender qué sucede o pasamos los días escribiendo código. Pero incluso si fuéramos capaces de hacer ambas cosas, no seríamos capaces de conocer todo.

¿Quién lo sabe todo? ¿Las inteligencias artificiales? No, ni siquiera ellas. Aprenden lo que pueden asimilar de la red, pero si el dato no está presente o se interpreta mal, el resultado será erróneo: existe un mundo de código en el ámbito legacy, sin documentación que las inteligencias artificiales no conocen. Están todos los productos de código cerrado que no pueden ser analizados, todos aquellos que aún deben ser lanzados y así sucesivamente.

Así que pongámonos en paz: no podemos saberlo todo y, incluso con las herramientas más modernas, nunca seremos capaces de conocer cada cosa. Siempre habrá grados de ignorancia o de error en todo el código que escribamos.

De la misma manera, todo lo que escribimos hoy podría resultar incorrecto: porque no conocemos plenamente un producto y porque la tecnología evoluciona y cambia, y lo que hoy se considera correcto, mañana podría ser considerado erróneo.

## Era ignorante y no lo sabía

Últimamente he trabajado en la optimización de un producto Java al que se le pedía ejecutar una serie de operaciones dentro del umbral de 10 milisegundos.

El código parecía correcto, pero ocasionalmente el programa superaba los 100 milisegundos. En un entorno donde incluso los milisegundos tenían un peso, esta oscilación no era tolerada porque superaba el SLA del servicio que debíamos proporcionar.

¿Cuál era el problema? La instanciación de un objeto llamaba al cargador de clases para buscar un cierto tipo de clase, en lugar de instanciar directamente una clase. Esta operación, que en el 99.999% de los casos se resolvía en menos de 1 milisegundo, en algunos casos llegaba a 100 milisegundos.

¿La solución? Evitamos la búsqueda de la clase de manera dinámica, pasando a una instanciación estática. Peso de la modificación: 1 línea de código, pero el retraso ocasional desapareció.

No conocíamos tan profundamente la clase que usábamos, y en condiciones normales el problema no existía: aparecía solo en momentos de estrés aplicativo en fuerte concurrencia.

¿Cómo lo entendimos? Hablándonos entre nosotros, confrontándonos, juntando nuestras habilidades y experiencias.

## La ignorancia es un recurso

En este mar de conocimiento – o de ignorancia, si se quiere ver el vaso medio vacío – lo único que podemos hacer es potenciar aquellas que son las habilidades blandas, en su momento subestimadas y hoy más que nunca esenciales.

Que quede claro: las habilidades técnicas son fundamentales, así como es esencial conocer y usar bien las nuevas herramientas que se nos ponen a disposición cada día, pero para quienes han pasado años trabajando con el código, hay habilidades que marcan la diferencia cuando se colabora en equipo.

Dado que libros, manuales e inteligencias artificiales nunca tendrán todas las respuestas, lo que más aprecio es el **coraje de preguntar**.

Hay habilidades y experiencias que residen solo dentro de las personas, y a menudo es más fácil preguntar a quien sabe en lugar de tratar de entender por uno mismo.

Por miedo a ser humillados o ridiculizados, no nos atrevemos a hacer una pregunta a un colega, no decimos "no entendí", no tenemos el coraje de pedir aclaraciones. Pasamos horas frente a piezas de código incomprensibles, pedimos ayuda de forma anónima en foros, Reddit, Stack Overflow o a varias inteligencias artificiales, pero en lugar de dirigir una simple pregunta al colega sentado junto a nosotros, preferiríamos casi prendernos fuego. No hacemos grupo y preferimos rompernos la cabeza solos frente a un problema.

El orgullo se transforma en una cadena invisible que nos limita, nos paraliza, nos hace desperdiciar tiempo valioso y nos induce a cometer errores evitables.

Tememos ser juzgados como débiles, pero en realidad, admitir que no se sabe es una gran virtud.

Una vez un antiguo filósofo dijo:

```text
Tu mantra para la vida debe ser "dignidad cero"
```

En realidad no era un filósofo, sino Mauro Repetto, fundador de los 883, pero el mensaje que llega es el mismo: **seguir tus sueños sin preocuparte por las críticas o el juicio ajeno**.

Muchas veces es de hecho el miedo al juicio lo que nos detiene y no nos permite crecer. Pero si no preguntamos, ¿cómo podemos aprender? Si no admitimos que no sabemos, ¿cómo podemos mejorar?

## Gestión de la ignorancia

Todos somos ignorantes, pero en temas diferentes. Admitir que no se sabe y manifestar este aspecto en la empresa a veces puede mover recursos.

Hace años me encontraba en una empresa donde habíamos decidido apostar por C++ para el nuevo producto que queríamos realizar: los motivos eran la velocidad de ejecución y la posibilidad de escribir código más cercano al hardware. Con el tiempo la elección se reveló equivocada, no por los supuestos iniciales, sino por el hecho de que se dirigía a un grupo de programadores que nunca habían trabajado con ese lenguaje y provenían de lenguajes más simples.

En ese momento la dirección se dio cuenta de una laguna: el equipo en el que estaba y que debía desarrollar en C++ no tenía, o tenía solo en parte, las competencias adecuadas para poder realizar el producto que nos habíamos propuesto. Por este motivo se organizó un curso con un experto del lenguaje, para desbloquearnos en toda una serie de aspectos que no habíamos considerado y no conocíamos.

Manifestar nuestra ignorancia nos hizo dar un salto adelante, nos permitió entender dónde estábamos fallando y corregir el rumbo, pero sobre todo nos hizo comprender que no estamos solos y que pedir ayuda es normal.

Si esto vale para un equipo, donde quizás es incluso más fácil preguntar, vale mucho también para los individuos.

## El coraje de preguntar

Hace años trabajaba para una empresa que había contratado a varios chicos recién graduados. Sus habilidades eran variadas: algunos ya demostraban cierto talento, otros menos. Sin embargo, uno en particular se destacaba de los demás no por sus capacidades técnicas – de hecho, tenía notables lagunas – sino por su extraordinaria predisposición a pedir aclaraciones, incluso repetidamente durante el día. Esta actitud, aparentemente simple pero en realidad revolucionaria, con el paso del tiempo lo llevó a superar a todos sus compañeros.

Su ChatGPT eran los colegas, las personas más experimentadas que él, que lo guiaban, le explicaban qué debía hacer y no hacer y dónde debía mejorar su estudio.

El miedo a hacer el ridículo es a menudo una jaula que nos mantiene atrapados en nuestra zona de confort. Tenemos una elección: permanecer prisioneros del miedo o liberarnos con el coraje de preguntar. El camino para convertirse en mejores programadores comienza aquí.

## El mito del sabelotodo

El mundo tech abunda en personas que se erigen como sabelotodos, convencidas de saberlo todo y de no necesitar ninguna ayuda externa. Esta peligrosa ilusión nace de una imagen distorsionada de la perfección. Consideren a los superhéroes como metáfora: se representan como seres perfectos, infalibles, autosuficientes e intrépidos. Pero no somos superhéroes con superpoderes: somos seres humanos, con todos nuestros límites y nuestras fragilidades.

Intenten mirar también a todas las personas que siguen en las redes sociales. A menudo parten de temas que conocen, son muy hábiles al hacerlo y gracias a esto atraen seguidores. Con el tiempo, de manera más o menos inevitable, la vena creativa disminuye y la búsqueda desesperada de temas interesantes lleva a hablar de cosas que no se conocen bien, pero que se piensa que pueden interesar.

En este punto la calidad se deteriora, pero dado que el público sigue apreciando y los seguidores aumentan, se persevera en este camino, hasta que uno se encuentra hablando de temas que no se conocen en absoluto.

Este es el momento en que uno se convierte en sabelotodo, se cree que se puede hablar de todo y saberlo todo, pero en realidad es solo un engaño.

Esta situación le ocurre más o menos a todos con el tiempo, pero es importante reconocerlo y no caer en la trampa del sabelotodo.

Si tu audiencia te ve como una guía, como un punto de referencia, es importante en algún momento detenerse, entender el propio límite, admitir que no se sabe y hacer intervenir a quien es experto en un cierto tema.

La diferencia entre un sabelotodo y un experto está aquí: si somos expertos y queremos lo mejor para un cierto tema, iremos a preguntar a quien, sobre un tema particular, es más competente que nosotros y sabrá mejor guiarnos, y no siempre se trata de una inteligencia artificial, sino de una persona física, con nombre y apellido.

## Preguntar solo no basta

¿Hemos encontrado el coraje de preguntar? ¿De hacer intervenir al experto? En este punto podría surgir un segundo problema: fingir entender.

Ya preguntar es un gran paso, pero admitir que no se ha entendido una respuesta es un segundo paso que a menudo no se da. Se prefiere fingir haber comprendido, aunque no sea así, por miedo a ser juzgados como tontos.

```text
Repetir y reformular
```

Una manera simple de verificar la comprensión de un concepto es repetirlo y reformularlo con nuestras propias palabras. Si no se logra hacerlo, significa que no se ha entendido bien y es necesario pedir más aclaraciones.

## La diferencia entre jamón cocido y jamón crudo

Yo no logro distinguir el jamón cocido del jamón crudo, es algo que llevo arrastrando desde hace muchos años. Mi cerebro se niega a asociar la palabra al producto. Sé lo que quiero, pero no logro asociar la palabra correcta.

```text
Pásame el jamón cocido
```

es una de las preguntas más embarazosas que me pueden hacer, porque sé que la respuesta será:

```text
Eso es jamón crudo
```

Con el tiempo entendí el problema: asociaba al color oscuro la cocción y al color claro la no cocción del alimento. Mi cerebro asociaba al contrario las palabras, e invertía el resultado, sabiendo que había algo que no iba bien, pero sin lograr entender qué.

A fuerza de equivocarme empecé a preguntar, y después de muchas explicaciones, muchos modos de recordar, entendí cómo distinguir el jamón cocido del jamón crudo: pero si no hubiera empezado a preguntar, quizás nunca habría tenido un mecanismo en la cabeza capaz de hacerme entender la diferencia.

## El miedo al juicio

Ser juzgados, ser vistos como el que no sabe, es un miedo que nos bloquea y nos impide crecer. Pero si no preguntamos, ¿cómo podemos aprender?

De la misma manera, si superamos este miedo en la pregunta, debemos superarlo también en la respuesta: no basta con preguntar, es necesario también entender la respuesta y admitir que no se comprende. Preguntar sin entender equivale a no preguntar, pero también admitir que no se ha comprendido la respuesta es un arte que debe ser aprendido con el tiempo.

## Cultura de avanzar a través del fracaso

Otro concepto que me fascina es el de la cultura de avanzar a través del fracaso, es decir, la cultura del fracaso. Fallar es normal, es humano, es un paso necesario para crecer y mejorar.

Admitir que no se sabe, equivocarse y usar el fracaso como trampolín para mejorar es una de las claves para convertirse en un mejor programador.

Desafortunadamente, no saber, fallar, mostrarse vulnerables todavía se percibe como un defecto: en realidad representa una poderosa herramienta para crecer, aprender y mejorar, una lección que debería ser transmitida desde la infancia.

```text
No te detengas por miedo a equivocarte, sino equivócate para aprender
```

## Conclusiones

La próxima vez que dudes en hacer una pregunta, pregúntate: ¿prefiero parecer momentáneamente inseguro o quedarme estancado para siempre?

Y si alguien se burla de ti por tus preguntas aparentemente ingenuas, recuerda que es precisamente él, al no hacerlas, quien se limita y construye lentamente una jaula invisible de la que será cada vez más difícil salir.

Nadie nace sabiendo todo, pero solo quien tiene el coraje de admitir que no sabe puede realmente aprender y crecer.
