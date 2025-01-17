# "Veamos quién la tiene más grande: hagamos revisión de código"

La revisión de código es uno de los momentos más delicados e importantes de un proyecto de software. Cualquier proyecto de software que hayamos desarrollado o desarrollemos en el futuro ha sido o será sometido a una revisión de código.

No es imaginable un código escrito por cualquiera que no sufra cambios con el tiempo. Aunque esto pueda ser cierto para partes individuales de un proyecto, si miramos la totalidad de un proyecto de software, la revisión de código se convierte en un paso significativo entre quedarse pequeño y jugar con muñecas, o salir a la luz y convertirse en adultos.

Este paso es, por lo tanto, fundamental para garantizar la calidad del código, para evitar que errores puedan comprometer el funcionamiento del software y para ampliar el conocimiento del código a todo el equipo. Sí, porque hacer evolucionar al equipo es un aspecto más importante que sublimar el propio ego al mirar unas pocas líneas que solo quien las escribió puede entender.

## La revisión de código molesta

Sin embargo, existe un problema de fondo: a los programadores la revisión de código les molesta, no les gusta, la consideran superflua o incorrecta si la hacen otros y creen que debe ser hecha y decidida solo por ellos.  
Para algunos, es como perder un hijo:

```text
Ese código estaba escrito de esa manera por una razón muy precisa: Mario no quería que nadie lo tocara, pero ahora que se ha ido, ya no se entiende nada.
```

Un buen momento para hacer revisión de código es cuando se corrige un error. Sin embargo, es necesario desmantelar el enfoque que a menudo adoptan los programadores, que tienden a ser quirúrgicos y a resolver la única notificación, sin aprovechar el pensamiento holístico.

```text
Me han informado que al hacer clic en un botón hay un error, me aseguro de que no lo haya.
```

En realidad, el problema podría ser mucho más profundo y requerir una reflexión más amplia. Deberíamos plantearnos el problema de por qué se hizo clic en ese botón, si fue clicado por un usuario, si fue clicado por un usuario que no debería haberlo hecho, si fue clicado por un usuario que no debería haberlo hecho en ese momento, si fue clicado por un usuario que no debería haberlo hecho en ese momento y en ese contexto.

Si queremos ampliar el pensamiento, podríamos preguntarnos si el problema no se extiende a otros botones, si y cómo se informa, si tiene sentido tener ese botón o esos botones que realizan esa operación, si la operación que realiza ese botón es necesaria, si la operación que realiza ese botón es necesaria en ese contexto.

Ampliar el contexto, sin embargo, significa gastar tiempo, emplear recursos, cuestionar el propio trabajo y el de los demás, significa cuestionar el propio ego y el de los demás, pero al hacerlo se mejora el código, se mejora el sistema, se mejora el equipo.

Por lo tanto, es necesario no mirar la única notificación que se nos hace, sino tratar de entender el contexto en el que se hizo y si hay otras partes del código que podrían mejorarse.

El pensamiento holístico, incluso en el código, es importante: si no entendemos que una sola modificación tiene un impacto en todo el sistema, no podemos entender el sistema, si no entendemos el sistema, no podemos mejorarlo.

Como decía Platón:

```text
El refactoring es el arte de quitar el mal y añadir el bien al código.
```

Quizás el autor no era Platón, pero el concepto es claro: el código debe mejorarse, debe hacerse más legible, más mantenible, más comprobable.

## El código no utilizado

Si has trabajado en el mismo proyecto durante más de un lustro, la frase:

```text
Ese código lo escribimos para un "Cliente importante", que ya no es nuestro cliente, pero no lo quitamos porque "podría" servir
```

es casi un mantra que estoy seguro has escuchado al menos una vez.  
Estratificar pensamientos de este tipo a lo largo del tiempo lleva a tener un código que no se entiende, que no se sabe qué hace, que no se sabe por qué lo hace y que no se sabe cómo lo hace: las especificaciones estaban entrelazadas con las necesidades del cliente, con las exigencias del equipo, con las decisiones técnicas del momento.

Mientras tanto, el código ha cambiado, el equipo ha cambiado, el cliente ha cambiado, las necesidades han cambiado, las decisiones técnicas han cambiado: es justo que el código cambie o sea eliminado del proyecto. Mantener código no utilizado es costoso y con el tiempo representa una deuda técnica innecesaria.

Hay empresas que han entendido lo costoso e inútil que es mantener proyectos que ya no se utilizan: el código es un costo, no un valor, si no se utiliza.

Google, por ejemplo, tiene una rica historia de proyectos que han sido abandonados. Puedes encontrar rastros de ellos en Wikipedia:

```text
https://en.wikipedia.org/wiki/Category:Discontinued_Google_services
```

## Yo uso TAB, quien usa espacios no es un buen programador

En un episodio de "Silicon Valley", el protagonista Richard descubre que su novia Winnie utiliza espacios en lugar de TAB para indentar el código y la deja: es una exageración cinematográfica, pero conozco personas que nunca aceptarían trabajar con alguien que usa espacios en lugar de TAB y viceversa.

Desmantelar este hábito, y lo dice alguien que usa espacios desde que puso el dedo en el teclado, es difícil, pero necesario: el código debe ser uniforme, debe ser coherente, debe ser legible. Tener estilos diferentes dentro del equipo es contraproducente, ralentiza el trabajo, aumenta la posibilidad de errores, dificulta el mantenimiento.

Dentro de una revisión de código es necesario discutir también estas cosas: no se trata de imponer un estilo propio, sino de encontrar un compromiso que pueda ser aceptado por todos y que, posiblemente, no sea una carga para nadie.

Una vez alcanzado un acuerdo, es importante respetarlo: si se decide usar espacios en lugar de TAB, no se puede retroceder.

Sin embargo, es algo difícil de aceptar y de implementar, tanto porque algunos programadores consideran el código como un hijo, que no se puede cambiar, como por el hecho de que, incluso imponiendo un estilo uniforme, tarde o temprano alguien no entenderá la especificación, otros configurarán el IDE de manera incorrecta o perderán las configuraciones en la primera actualización.

En estas situaciones, donde no es el propio lenguaje el que nos ayuda a mantener un estilo uniforme (sí, hay lenguajes que lo hacen por nosotros de manera absolutamente dictatorial), es importante utilizar herramientas que nos permitan automatizar lo más posible la formateo del código.

Dentro de uno de los proyectos más grandes que sigo, se decidió adoptar OpenRewrite, una herramienta que reformatea el código de manera automática, uniforme y coherente, reduciendo las diferencias entre diferentes estilos de programación: uniformar, además de hacer el código más coherente, acelera la incorporación de nuevos miembros al equipo y el traspaso de un componente de un equipo a otro.

## Resistencia al cambio

Aunque la mayoría de los programadores está de acuerdo en la necesidad de una revisión de código, a menudo se niegan a aceptar los cambios propuestos, un poco por pereza, un poco por orgullo, un poco por costumbre.

Si has trabajado durante años de la misma manera, y funciona, ¿por qué cambiar?

```text
Mi código nace perfecto
```

Desafortunadamente no: no es así. Dentro de un equipo, el aspecto que debe prevalecer es la lectura del código por parte de todos, debe prevalecer la facilidad de incorporación de un nuevo recurso, debe prevalecer la simplicidad de modificación incluso después de meses de no tocar algunas líneas.

Por lo tanto, no importa si el IDE que usas formatea el código de cierta manera, no importa si siempre te ha gustado declarar variables con "_", adherirse a un estándar difundido, espontáneamente o a través de automatizaciones, es una ventaja, incluso si al principio puede parecer una carga.

## Código limpio

Uno de los objetivos que debería tener una revisión de código es escribir código limpio, legible y mantenible.

A veces me he encontrado ante la elección de mantener un código que funcionaba, o desmontarlo porque, aunque superaba de manera excelente cualquier prueba funcional, estaba escrito de manera oscura, difícil de leer y de mantener, y cada vez que ponía a una persona frente a ese código, su expresión siempre era la misma:

```text
No entiendo qué hace
```

A veces creemos que usar la última sintaxis propuesta por un lenguaje es la solución a todos nuestros problemas, pero no siempre es así. A veces los nuevos constructos se basan en conceptos difíciles de comprender y de explicar, a veces son solo caramelos para hacernos sentir más hábiles: "sugar code" como lo llaman algunos.

No siempre el código más compacto y conciso es el mejor: a veces es mejor escribir 10 líneas de código que hacen lo que deben de manera clara y legible, en lugar de una sola línea que hace lo mismo, pero que nadie entiende, para no ganar nada a nivel de rendimiento y funcionalidad.

## Automatizar lo posible

Curiosamente, los programadores aceptan de buen grado algo que es propuesto por un programa, en comparación con lo que es propuesto por alguien dentro del equipo.

Si en tu equipo también hay el mismo clima, puedes proponer la introducción, dentro de la línea de proyecto (esperando que tengas una), de procesos de normalización de código y análisis estático.

Los primeros servirán para disminuir la diferencia de estilo entre un programador y otro, los otros servirán para sugerir modificaciones, para hacernos entender dónde están ocultos los errores, dónde faltan pruebas, dónde la complejidad cognitiva es demasiado alta o dónde podemos reducir el código, sin perder claridad o eficacia.

## Pero a mí no me interesa

De vez en cuando paso mi tiempo libre estudiando proyectos de otros programadores, hago correr algún analizador y trato de corregir un poco de código: es un buen entrenamiento y me permite ver cómo otros abordan los problemas o subestiman las consecuencias de su código.

Durante estas incursiones, me he encontrado con enfoques completamente diferentes por parte de programadores individuales o equipos de programadores a los que presentaba mis Pull Requests.

De todos los proyectos que he analizado, me gustaría hablar de dos que me han impresionado particularmente por cómo el equipo gestionó mi contribución.

La primera Pull Request se refiere al JDK de OpenJDK. Me di cuenta de que, por distracción, 82 fuentes contenían dobles ";" al final de una línea.  
Entiendes que no se trata de algo importante, podemos incluso decir que se trata de algo insignificante, pero decidí hacer una Pull Request para corregir el problema y ver cómo se comportaría el equipo de desarrollo.

Puedes encontrar la PR en esta dirección:

```text
https://github.com/openjdk/jdk/commit/ccad39237ab860c5c5579537f740177e3f1adcc9
```

El enfoque, en mi opinión, fue interesante: primero se involucraron en el análisis de la modificación 8 personas, siendo las modificaciones horizontales a muchos paquetes de Java.  
Después de una discusión horizontal de varios mantenedores y haber constatado que el problema era real, se abrió un issue:

```text
https://bugs.openjdk.org/browse/JDK-8282657
```

También se discutió una posible modificación a las herramientas de construcción, que ya eliminaban los espacios al final de la línea, introduciendo la eliminación de los caracteres dobles ";".

Este enfoque denota un equipo que analiza cada modificación individual, que discute y que trata de entender si la modificación propuesta es realmente útil o si es solo un capricho de alguien.  
En este caso, entendieron que se trataba de una modificación trivial, pero orientada a la limpieza del código, y por eso fue aceptada.

Un segundo caso, sin embargo, involucra una herramienta de seguridad realizada por un único mantenedor, también puesta en GitHub.  
En ese caso, había propuesto una PR mucho más seria. Había código redundante, se utilizaban clases sincronizadas en procesos en los que no se necesitaba sincronización, algunos recursos se abrían sin un cierre explícito y así sucesivamente.

Por lo tanto, se trataba de una modificación orientada a mejorar la calidad del código y a reducir la posibilidad de errores, no algo trivial como la eliminación de un carácter.  
Además, el paso a objetos no sincronizados llevaba a un aumento de rendimiento en torno al 20%: todo esto sin desnaturalizar el código, sino solo utilizando los constructos correctos y, a igualdad de interfaces, las clases correctas.

En este caso, estaba convencido de que no habría problemas para insertar este código en el proyecto, pero la respuesta fue negativa.  
El mantenedor respondió que no tenía intención de integrar en su código las sugerencias que derivaban de un analizador sintáctico y que podía usarlas en mi fork y él nunca las integraría.

```text
Si no te gusta mi código, haz tu fork y modifícalo como quieras
```

Esta es la clásica respuesta de quien no quiere cambiar, de quien no quiere aceptar que su código pueda ser mejorado, de quien no quiere aceptar que su código pueda ser cambiado por otros, a pesar de que las modificaciones puedan mejorar la legibilidad y traigan mejoras tangibles.

## Conclusión

Incluso cuando todo funciona, revisar el código es importante: permite mejorar el proyecto, mejorar el equipo y reducir lo que son las deudas técnicas.

Disminuir la deuda técnica, tener el coraje de desmontar incluso código que funciona, eliminar código que ya no se usa, escuchar a los revisores estáticos, uniformar el estilo de programación, automatizar lo más posible la formateo del código, son todos pasos que pueden mejorar el código y el equipo.

No tengas miedo de cuestionar lo que se escribió en el pasado y amplía la visión cuando debas poner manos al código: no mires solo la modificación individual, sino trata de entender el contexto en el que se hizo y si hay otras partes del código que podrían mejorarse.

Un producto mejor pasa por muchos pequeños pasos y no se dice que, a pesar de tener cientos de pruebas funcionando, el código sea perfecto: la revisión de código es un paso fundamental para garantizar la calidad del código y para evitar que errores puedan comprometer el funcionamiento del software.
