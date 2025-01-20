# La adopción de nuevos frameworks podría hacer fracasar tu proyecto

En el mundo del desarrollo de software, la atracción por las novedades siempre es fuerte. Es tentador poner las manos en un nuevo producto, tal vez el primero en resolver una serie de problemas que otros frameworks no pueden abordar.

Estos nuevos proyectos a menudo cuentan con una comunidad pequeña pero enérgica, prometen acelerar los tiempos de desarrollo y presentan innovaciones interesantes en comparación con los competidores. Todo esto parece muy prometedor, pero ¿es realmente la elección correcta para un proyecto a largo plazo?

Donald Knuth, uno de los padres de la informática moderna, comentaba su propio código de esta manera:

```text
Presten atención a los errores en el código anterior; solo he demostrado que es correcto, no lo he probado.
```

Si esta frase hubiera sido escrita por un programador junior, podría parecer una broma. Pero dicha por Knuth, además de ser humorística, podría también señalar que esa parte del código no era testeable, sino solo sintácticamente correcta.

A veces es mucho más sencillo demostrar un concepto, describir su funcionamiento y documentarlo, en comparación con su aplicación real, que podría involucrar una serie de aspectos no considerados en la demostración.

Este concepto se puede parafrasear así: "No es seguro que una idea brillante funcione siempre en la realidad". Pensando en esto, no puedo evitar considerar el mundo de las blockchain: en teoría, herramientas excelentes, pero en la práctica a menudo criticadas por su rendimiento y uso de recursos.

Saliendo del mundo del software, pensemos en productos como el Segway que, a pesar de ser una idea brillante, no tuvo el éxito esperado. O en Google Glass, que a pesar de ser un producto innovador, nunca despegó.

## ¿Y los frameworks?

Los frameworks y, más en general, las tecnologías de software, a menudo sufren de un hype inicial que entusiasma a los programadores, distrayéndolos de un análisis sólido de su eficacia a largo plazo. ¿Los conceptos utilizados en ese nuevo software son aplicables a todos los proyectos? ¿Son fácilmente integrables con otras tecnologías? ¿Hay empresas sólidas que invierten en esa tecnología? ¿La comunidad es activa y apoya el producto?

Los llamados "early adopters" a menudo se sienten atraídos por las novedades, pero frecuentemente no se dan cuenta de los riesgos que esta elección conlleva. Si todo va bien, han hecho una elección afortunada que ha llevado al éxito su software. Pero si el producto elegido no cumple con las promesas, se encuentran con un software que no funciona como debería y que requiere un trabajo de mantenimiento y refactorización mucho más pesado de lo previsto.

Para quienes desarrollan software desde hace más de 30 años, el nombre Visual Objects hará sonar algunas campanas: debía ser el nuevo Clipper y llevar a millones de programadores DOS al entorno Windows. Una idea fantástica, pero que no funcionó: demasiados problemas, demasiados errores, demasiados límites. En su momento, tenía detrás una empresa como Computer Associates, que podía permitirse invertir millones de dólares en un producto, pero a pesar de esto, nunca despegó.

Por eso, cuando se trata de elegir un framework o una tecnología para un proyecto, es importante considerar no solo sus características técnicas, sino también su sostenibilidad a largo plazo.

![Frameworks](06-EsplorareNuoviFramework-articolo-1-leonardo-ai.jpg)

## El horizonte temporal: una dimensión crucial

Cada vez que evalúo un proyecto, trato de anticipar su ciclo de vida, o al menos lo que debería ser, basándome en la experiencia y en la información a mi disposición. La bola de cristal no existe y el futuro no es predecible, pero hay señales que permiten entender si un proyecto será de corta, media o larga duración.

Para comprender cuánto puede durar un proyecto, es importante considerar varios aspectos:

- **Objetivos a largo plazo**: ¿Cuáles son los objetivos del proyecto? ¿Es un producto que resuelve un solo problema o algo estructurado para durar años o solo unos pocos meses?
- **Estabilidad del mercado**: ¿El mercado en el que opera el proyecto es estable o está en rápida evolución? La efervescencia de un mercado puede llevar a cambios rápidos que requieren una mayor flexibilidad por parte del proyecto.
- **Competencia**: ¿Cuál es el nivel de competencia en el sector en el que opera el proyecto? Trabajar en una arena donde tal vez los otros actores provienen de empresas más grandes y estructuradas puede requerir una mayor atención a la calidad y la sostenibilidad del proyecto.
- **Tendencias del sector**: ¿Cuáles son las tendencias actuales en el sector en el que opera el proyecto? Algunos proyectos nacen ya viejos, porque se basan en tecnologías obsoletas o en modelos de negocio superados.
- **Recursos disponibles**: ¿Qué recursos están disponibles para el desarrollo y mantenimiento del proyecto? ¿Se trata de proyectos "one man show" o hay equipos estructurados detrás?

Estos son solo algunos de los indicadores posibles, pero basarse solo en el nombre y en lo que se promete a menudo es una subestimación del riesgo.

Cuando se utilizan frameworks o tecnologías jóvenes, es importante considerar que podrían no ser soportados a largo plazo o podrían no ser capaces de adaptarse a los cambios del mercado. Esto puede llevar a costos de mantenimiento elevados, problemas de compatibilidad y una mayor complejidad del código.

Por otro lado, también es necesario evaluar los proyectos que se pretenden realizar. Podrían ser proyectos nacidos y concluidos en el transcurso de un fin de semana: en este caso, la necesidad primaria es la resolución del problema. Otros podrían tener que durar unos pocos meses para satisfacer una necesidad específica. Finalmente, existen proyectos destinados a durar años, sobre los cuales una empresa pretende construir su base operativa: en estas situaciones, la elección del framework y la arquitectura del proyecto se vuelve crucial y no puede basarse solo en la moda del momento.

El horizonte temporal es una dimensión que todo arquitecto de software debería tener en cuenta, porque influye notablemente en las expectativas y las decisiones que se pueden tomar.

Para un proyecto "one-shot", se puede adoptar tranquilamente el framework CIRO, creado por un nómada de Tanzania, utilizado solo por su grupo de amigos, con un único lanzamiento hecho hace algunos años, si resuelve de manera asombrosa un problema crucial para el proyecto. Si en cambio debo realizar algo que debe durar más allá de la fecha de caducidad de un postre, tal vez debería moderar mi agresividad en la elección de los componentes de software a emplear y basarme en KPI diferentes.

## El riesgo del abandono

Me ha sucedido usar productos tanto "closed source" como "open source", cuyo creador desapareció en la nada, así como se disolvió la comunidad que formaba parte de ellos. Si esto ocurre con productos "closed", es ciertamente muy preocupante, pero no caigan en la ilusión de que todo es color de rosa si ocurre con productos "open". Una cosa es utilizar un producto, otra es desarrollarlo y conocerlo en cada uno de sus detalles.

La mente de quien diseña una solución suele estar atrapada entre las líneas de código del propio producto y está ciertamente más inmersa en sus lógicas internas que quien lo usa, que a menudo aprovecha solo una parte de sus potencialidades. No piensen entonces que "open" significa "hay un problema: lo resuelvo yo", porque no siempre es así.

Linus Torvalds, creador de Linux, tiene una opinión fuerte sobre este tema:

```text
El software es como el sexo: es mejor cuando es libre y gratuito.
```

Aunque Torvalds utiliza esta cita para promover el software open source, es importante recordar que "gratuito" no significa necesariamente "sin costos" y que la libertad de disponer de los fuentes de un proyecto no necesariamente significa poder mantenerlo y hacerlo evolucionar.

## La importancia del análisis periódico

Este es uno de los motivos por los que siempre deberíamos realizar un análisis de la vida de los productos que adoptamos. Un análisis a repetir periódicamente, que tenga en cuenta el contexto actual, la madurez del proyecto y sus perspectivas futuras.

Si en los proyectos cortos se puede ignorar este aspecto, en aquellos que superan los años de desarrollo, el problema se vuelve inminente: o se actualiza el producto y sus dependencias, o se encuentra uno en un callejón sin salida debido a los innumerables entrelazamientos de su propio código.

Un análisis periódico nos permite evaluar si el framework o la tecnología que estamos utilizando sigue siendo adecuada para nuestras necesidades, si está soportada activamente por la comunidad y si es capaz de adaptarse a los cambios del mercado.

## El riesgo de los servicios no estándar

Esto se aplica también a todos los problemas que pueden surgir de la adopción de un servicio sin estándar, que podría ser retirado del mercado o duplicar los precios de una temporada a otra.

Jeff Bezos tiene una visión interesante sobre cómo las empresas deberían abordar la tecnología:

```text
Hay que ser testarudos en la visión y flexibles en los detalles.
```

Esta filosofía puede aplicarse también a la elección de frameworks, servicios y desarrollo de software: mientras los detalles técnicos pueden cambiar, los principios básicos como la escalabilidad, la mantenibilidad y la interoperabilidad deberían permanecer constantes.

Por este motivo, realizar un software fuertemente acoplado con un framework podría llevar a problemas de mantenimiento y escalabilidad en el futuro. Si el framework ya no es soportado o no es capaz de adaptarse a los cambios del mercado, podríamos encontrarnos en una situación en la que es necesario reescribir gran parte del código para adaptarlo a una nueva tecnología.

He visto productos tomar decisiones técnicas que, en teoría, parecían las mejores, y con el tiempo darse cuenta de que el acoplamiento de software que se había realizado era tan fuerte que cambiar una parte significaba tener que cambiar todo lo demás. Este problema también se puede evitar con un análisis correcto y una elección ponderada de los componentes utilizados, desacoplando uso de implementación y aceptando tener que cambiar una parte del software si es necesario.

## Conclusión

Cuando se trata de soluciones o frameworks jóvenes, el riesgo de desperdiciar tiempo y recursos es considerable. Si amas la incertidumbre y la duración del proyecto no es un factor que quieres considerar, eres libre de hacer cualquier elección y construir un producto lleno de preguntas sin respuesta.

En caso de errores, ten en cuenta que podría ser necesario empezar de cero, a menos que tu software sea lo suficientemente modular como para permitir la sustitución de un componente sin tener que reescribir todo lo demás.

La elección de un framework o una tecnología debería estar guiada no solo por el entusiasmo por la innovación, sino también por una evaluación ponderada de los riesgos y beneficios a largo plazo. La sostenibilidad, la mantenibilidad y la escalabilidad deberían estar siempre en la cima de nuestras prioridades cuando tomamos decisiones arquitectónicas.
