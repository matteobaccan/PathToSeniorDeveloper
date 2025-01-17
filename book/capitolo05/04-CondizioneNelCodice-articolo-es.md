# ¿Puedes cambiar esta condición en el código? ¿Qué se necesita?

¿Qué diferencia a un programador senior de un programador junior? Muchos dirán que es la capacidad de evaluar las consecuencias de una modificación en el código, pero en realidad es la pérdida de despreocupación y un conjunto de miedos regresivos.

## El miedo de los senior

Antes solía ser mucho más rápido al cambiar un algoritmo, al modificar un parámetro de una función, al crear o destruir flujos, y así sucesivamente. El objetivo era, ante todo, hacer lo que pedía el cliente y solo en segundo lugar asegurarse de que el código fuera mantenible o de que la elección tomada fuera la mejor dentro de una serie de opciones más o menos ponderadas.

Luego envejecí y comencé a usar pruebas para entender si mi código seguía siendo bueno después de una modificación, empecé a escribir documentación para entender por qué había razonado de cierta manera y comencé a hacer revisiones de código para mejorar la comprensión del código y su mantenimiento.

Este nuevo enfoque "complicó" mi trabajo, o mejor dicho: alargó los procesos que, desde una solicitud, llevaban a la solución final. Una modificación que antes hacía en 10 minutos, ahora ocupa un día entero, porque debo evaluar todos los impactos que esa modificación puede tener, ejecutar todas las pruebas automatizadas, realizar algunas pruebas manuales donde no pude automatizar, escribir la documentación, hacer el merge con el código principal, esperar la compilación y las pruebas de integración, verificar que todo funcione y finalmente declarar que el problema está resuelto, esperando no haber olvidado algo.

Los años pasan y es inevitable que haya una evolución desde el niño despreocupado que hace un push sin pruebas, hasta el cariatide que ajusta incluso los espacios cuando debe agregar código a la rama principal (no, ya no se usa "master").

```text
Lo que una vez fue un "sí" feliz y entusiasta,
se convierte en un "sí, pero también hago esto",
poco a poco se convierte en un "tal vez",
hasta llegar a un "no"
o peor aún un "depende".
```

## Los senior no son malos

No es por maldad que todo esto sucede, es por la conciencia de todo lo que rodea a una sola línea de código. La conciencia del error o de los impactos de una modificación y por un vasto retroceso que muchas veces ha minado la certeza de que una sola condición pueda cambiarse sin problemas. Esto no significa que las modificaciones no deban hacerse, solo significa que siempre se deben evaluar los impactos, para no crear problemas más grandes de los que se pretenden resolver y que a menudo, cuanto más se envejece, más se multiplican los impactos en la mente del programador.

Pensemos en el ciclo de vida de un software y en su diseño. Al principio, desarrollar un producto es relativamente fácil: vemos nuestro objetivo, tenemos una idea de cómo alcanzarlo, nos aseguramos de que los clientes y las partes interesadas estén satisfechos, y si tenemos suerte logramos crear un equipo cohesionado en el producto tanto desde el punto de vista técnico como humano. Esto no siempre es seguro porque a veces basta un solo elemento discordante capaz de desestabilizar a todo un grupo. Una vez alcanzado este objetivo, cuando se necesita hacer una modificación, todos los miembros están alineados y conscientes de lo que se necesita lograr.

Cuando se sale de esta fase de euforia colectiva y se abandona la fase creativa, el equipo de desarrollo comienza a cambiar en comparación con su forma original. Al mismo tiempo, el cliente reduce el presupuesto, porque se entra en una fase de mantenimiento y si no se presta la debida atención, se comienza a perder el dominio del producto.

```text
No, ciertamente no son las pruebas las que pueden gobernar el producto,
sino las mentes que lo han ideado.
```

El cambio de proyecto es un proceso inevitable, a menos que te encuentres en un iglú en medio del polo, sin conexión a internet, y los pobres programadores que han realizado el proyecto no puedan enviar un currículum si no es atándolo a una foca (aunque siempre existe la posibilidad de que el programador se dedique a la pesca, su gran pasión adormecida por el código).

Cuando se cambia un componente del equipo, se pierde una parte del conocimiento del producto y se comienza a perder el dominio del mismo. En cascada, cada intervención se vuelve cada vez más costosa, larga y arriesgada.

## ¿El mantenimiento de un proyecto cambia las reglas?

En un ciclo de vida normal de un producto, sucede que algunas partes están sujetas a actualizaciones frecuentes, pero muchas otras partes, por cuestiones de madurez, falta de demanda o estabilidad, no necesitan modificaciones. Hacer menos modificaciones disminuye el conocimiento del código por parte del propio programador que lo escribió. Esto significa que la persona que escribió esas líneas de código hace 2 años es normal que no las recuerde y necesite revisarlas para recordar los procesos que llevaron a su creación.

Cuanto más vertical es la modificación, más difícil es recordar la razón: no recuerdas por qué dentro de una conexión a un recurso externo pusiste un parámetro en lugar de otro, por qué usas una suite de cifrado en lugar de otra o tal vez tienes una rama abierta desde hace meses, esperando una verificación con un cliente sobre una funcionalidad urgente, que de repente se vuelve de poca importancia, pero ahora necesitas hacer el merge en una línea base con 400 push más y te preguntas si tiene más sentido empezar de nuevo o aplicar los cambios a un rebase.

En medio de este tipo de intervenciones están los trabajos diarios, las modificaciones a las funcionalidades, las correcciones de errores, las solicitudes de nuevas funcionalidades, las correcciones de nuevos errores que has introducido al corregir un error, el código que ha introducido un colega con poco conocimiento del producto, los cambios de comportamiento introducidos por el uso de una actualización o un nuevo componente que obliga a un cambio de código e introduce una anomalía indirecta.

Tú que escribiste ese código no lo recuerdas, entiendes que ante una serie de cambios la modificación a realizar es más grande de lo que se proyectaba, pero debes entender cómo hacerlo, porque tienes un recuerdo de los racionales por los cuales se hizo el código anterior y entiendes que no es una modificación trivial. Imagínate quien tiene que arreglar el mismo código y es la primera vez que pone las manos en esa parte del programa.

Como decía Heráclito:

```text
Ningún hombre puede cruzar el mismo río dos veces,
porque ni el hombre ni el río son los mismos
```

Esta frase se puede aplicar fácilmente al código: cada modificación, incluso la más pequeña, cambia el código y el contexto en el que se encuentra, que es diferente al contexto en el que fue creado, y también la persona es diferente a la persona que escribió ese código.

## Caso de uso de un conocido banco italiano

Por un momento, imagina ser un programador senior de un "banco cualquiera", donde te han dicho que debías proceder con una actualización del sistema y su firmware, que no causaría ningún daño y que se procedería a realizar la actualización en producción. Al haber visto este tipo de intervenciones varias veces en tu vida, lo primero que se te ocurre hacer es realizar una prueba, pero no existe un entorno de prueba que cubra exactamente las dimensiones de producción, ya sea por dimensionamiento o por casos de uso. Desaconsejas la actualización masiva, pero el fabricante de la solución asegura que no habrá problemas, el departamento de seguridad te avisa que es necesario implementar la actualización antes de una fecha específica porque de lo contrario no se cumplirían las normas de la empresa y que de todas formas, en caso de problemas, se puede retroceder.

A regañadientes aceptas, también impulsado por el hecho de que "trabajamos con la metodología ágil y debemos estar listos para el cambio" y que "no podemos ser siempre negativos".

```text
Las interrupciones en los accesos a los servicios en línea (como la aplicación, la aplicación de inversión, la banca por Internet y Smart Business)
ocurrieron después de la instalación de una actualización del sistema operativo
y su firmware correspondiente que provocó una situación de inestabilidad.
Queremos disculparnos nuevamente y consideramos fundamental agradecerte por la comprensión demostrada.
```

Una "simple" actualización del sistema operativo y el firmware provocó una situación de inestabilidad durante 5 días.

Claramente, en este caso hipotético, el problema no fue la actualización, sino la falta de pruebas, la falta de un entorno de prueba que cubriera la producción, la falta de un rollback inmediato y la falta de un plan de recuperación ante desastres o la subestimación del riesgo.

## ¿Cuál es la percepción de la modificación fuera del proyecto?

A menudo, quienes están fuera del proyecto tienen una percepción completamente diferente del desarrollo de software y presionan para realizar modificaciones lo antes posible.

```text
Lo necesito para ayer
```

Esta frase es un clásico, pero a menudo no se entiende que una modificación, incluso banal, puede acarrear una serie de problemas que van mucho más allá de la modificación en sí misma.

```text
Solo pedí cambiar una condición, ¿por qué Mario me está causando todos estos problemas?
Ahora asigno la tarea a Bruno, quien lo resuelve en 2 minutos
```

Hay situaciones dentro de los proyectos que permiten alterar el código muy rápidamente, y otras situaciones en las que una modificación, incluso banal, puede requerir mucha reflexión: incluso si se trata de unas pocas líneas de código o incluso una sola condición adicional. Cada programador aborda la modificación de manera diferente, según su experiencia, el conocimiento del producto y el conocimiento del código. Cuantos más programadores experimentados haya en el producto, es más probable que la modificación se evalúe cuidadosamente, porque se es consciente de lo que una modificación puede implicar. Cuanto menos conozca el programador el producto, es más probable que la modificación se realice rápidamente.

## Conclusiones

Cada modificación, incluso la más banal, puede acarrear problemas de rendimiento, regresión, seguridad, mantenibilidad, comprensión del código, documentación, pruebas, implementación.

De la misma manera, las alteraciones externas al proyecto pueden crear los mismos problemas: he actualizado el sistema operativo, he actualizado un controlador, he actualizado el firmware y ahora nada funciona.

La presión que se ejerce sobre un programador aumenta progresivamente con el tiempo porque paralelamente aumenta la conciencia de todo lo que puede salir mal y de lo difícil que es resolver un problema una vez que se ha producido.

Esto puede llevar a situaciones en las que un programador senior se niega a hacer una modificación, porque sabe que los riesgos son demasiado altos, o porque sabe que la modificación requeriría demasiado tiempo y recursos para hacerse correctamente.

La próxima vez que mires a un programador que ha estado trabajando en el mismo código durante muchos años y no quiere modificarlo y te advierte sobre cada alteración interna o externa al proyecto, no pienses en él como alguien incompetente, sino más bien como una persona consciente y utiliza su consejo para evitar que tu proyecto se derrumbe y para sopesar adecuadamente los riesgos y beneficios de cada modificación, porque al fin y al cabo, como dijo Isaac Asimov:

```text
Ninguna decisión sensata puede ser tomada sin considerar
no solo el mundo tal como es ahora, sino cómo será
```
