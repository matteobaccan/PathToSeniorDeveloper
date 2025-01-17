# El "celodurismo" de los programadores

En el mundo de la programación, existe un fenómeno curioso que podríamos definir como "celodurismo". Este término describe una actitud de obstinada resistencia a la evolución de las herramientas y prácticas de desarrollo de software.

En tiempos pasados, cuando los recursos eran escasos y valiosos, los programadores debían ser increíblemente ingeniosos para exprimir cada gota de potencia de sus sistemas. Esta necesidad forjó hábitos y mentalidades que, en algunos casos, han sobrevivido mucho más allá de su utilidad práctica, transformándose en una especie de folclore profesional.

```text
640K ought to be enough for anybody
```

Esta célebre frase atribuida a Bill Gates, aunque él ha negado su autoría, representa bien la actitud de muchos "celoduristas" hacia la innovación tecnológica. Para estos programadores, la idea de utilizar herramientas modernas como IDE avanzados, depuradores gráficos o asistentes de IA parece casi una herejía, una violación de los principios fundamentales de la programación "verdadera", un síntoma de debilidad e incapacidad.

## Las raíces históricas

En los albores de la informática, cuando las computadoras se alimentaban a base de tarjetas perforadas, programar significaba trabajar con sistemas dotados de memoria y procesadores limitados. Los programadores de la época debían ser verdaderos artistas de la optimización, capaces de escribir código que fuera a la vez funcional y extremadamente eficiente.

Esta era produjo obras maestras de ingenio y prácticas que aún sobreviven en entornos con recursos limitados: ¿alguna vez has intentado programar para microcontroladores o sistemas embebidos? Aquí, cada byte de memoria y cada ciclo de reloj cuentan, y el arte de la optimización sigue gozando de buena salud, aunque ya se empiezan a ver algunas grietas en el horizonte.

Con el paso del tiempo y la evolución del hardware, muchas de estas limitaciones han desaparecido, pero la ética del "hacer más con menos" ha quedado profundamente arraigada en la cultura de la programación, a veces transformándose en una actitud de resistencia hacia herramientas y prácticas que podrían simplificar y acelerar el trabajo de desarrollo.

```text
"El código más eficiente es el que no tienes que escribir"
```

## El manifiesto del celodurismo

Para entender qué tipo de programadores sois, aquí tenéis una pequeña prueba para evaluar vuestro grado de "pureza".
Intentad determinar cuánto estáis a favor o en contra de estas afirmaciones:

### 1. El IDE no sirve para nada

Un programador debe ser espartano: cuantos menos herramientas use, más competente es.

```text
"Para escribir código me basta con Notepad (o Vi) y la CLI"
```

Esta afirmación se pronuncia a menudo con una mezcla de orgullo y nostalgia. Quien la sostiene parece querer comunicar: "Soy un verdadero programador, no necesito ayudas". Esta posición ignora deliberadamente las ventajas que ofrecen los IDE modernos.

Personalmente, he visto programadores usar comandos como:

```text
copy con: pippo.prg
```

con el mismo orgullo de quien obtiene una excelente calificación en la escuela.

No subestimemos, sin embargo, las ventajas de los IDE modernos y, como primera cosa, quitémonos de la cabeza que los IDE son simples editores de texto con algunos adornos. Son herramientas poderosas que integran numerosas funcionalidades para mejorar la productividad y la calidad del código:

- Depuración: Puntos de interrupción, inspección y alteración de variables en tiempo real, ejecución paso a paso del código, pila de llamadas y mucho más.
- Refactorización: Renombrar variables o funciones en todo el proyecto con un solo clic, extrayendo métodos o reorganizando el código de manera segura.
- Análisis estático: Identificación de posibles errores, violaciones de estilo o patrones problemáticos antes de la ejecución.
- Integración con sistemas de versionado: Gestión de ramas, commits y merges directamente desde la interfaz del IDE.
- Soporte para frameworks y bibliotecas: Autocompletado, no solo de las bibliotecas base, sino también sugerencias específicas para los frameworks utilizados en el proyecto.

Estos son solo algunos de los motivos por los cuales, cuando entro en un editor inventado en los años 70, me siento como si me hubieran quitado un brazo.

Para ser intelectualmente honestos, no podemos negar que, en algunas situaciones, un IDE podría ser excesivo, como cuando se necesita hacer una modificación rápida o cuando se trabaja en sistemas remotos con recursos limitados. En estos casos, editores minimalistas o cualquier cosa que abra una consola textual podrían ser la mejor opción.
Para el trabajo diario y para proyectos de cierta complejidad, rechazar categóricamente el uso de un IDE moderno significa privarse de herramientas que pueden mejorar significativamente la calidad del código y la productividad del programador y de todo el equipo (sí, porque el código no es solo tuyo, sino de todos los que trabajan en él).

### 2. La CLI es la solución a todos los problemas

No nos engañemos, la CLI tiene un encanto innegable. Años de películas con hackers inclinados sobre teclados mecánicos y pantallas negras con letras verdes han formado generaciones de programadores. ¿Qué hay más poderoso que controlar una computadora escribiendo comandos textuales?
Este enfoque, aunque tiene el encanto del primer amor del instituto, tiene una serie de limitaciones que a menudo se pasan por alto:

- Curva de aprendizaje: Memorizar unos pocos comandos es fácil, memorizar decenas o cientos de comandos, con todas sus opciones, puede ser desalentador para los novatos y para quienes no usan la CLI diariamente.
- Visualización de datos: Algunas informaciones son simplemente más fáciles de comprender cuando se presentan gráficamente.
- Operaciones complejas: Ciertas actividades, como la gestión de ramas en un repositorio Git, pueden volverse mucho más intuitivas con una representación visual.

Git es un excelente ejemplo de cómo CLI y GUI pueden coexistir y complementarse mutuamente. Mientras que la CLI de Git ofrece un control granular y la posibilidad de automatizar operaciones a través de scripts, herramientas GUI como las integraciones en VSCode pueden hacer más accesibles operaciones complejas como:

- Visualizar el historial de commits con un gráfico de ramas
- Realizar rebase interactivos
- Resolver conflictos de merge con herramientas de diff visual

Como siempre, la verdad está en el medio y el enfoque más sabio es dominar ambas herramientas. Usar la CLI para operaciones rápidas y para crear scripts automatizados, pero no dudar en pasar a una GUI cuando esta puede ofrecer una visión más clara o un flujo de trabajo más eficiente.

### 3. No usamos Windows porque los programadores usan Linux (o MacOS)

Ya no cuento las noches que he pasado leyendo y comentando las "guerras de religión" de los sistemas operativos.

```text
"Winzoz" no funciona
Será bonito Linux que tiene 200 versiones y todas incompatibles
Dejadlo, con MacOS todo funciona
Mira que Apple te hace pagar el doble de lo que vale ese ordenador
```

Se podría seguir indefinidamente, creando flames llenos de odio y cargados de ignorancia, pero la realidad es que cada sistema operativo tiene sus pros y contras, y es erróneo sostener que uno es superior a los otros de manera absoluta.

Un programador debería estar por encima de estas charlas de bar. Esto no limita su libertad de sentirse cómodo en un sistema en lugar de otro, pero es absolutamente contraproducente ponerse anteojeras e ignorar la existencia de otros sistemas operativos además del preferido.

Reflexionemos sobre el hecho de trabajar diariamente en plataformas diferentes y de las ventajas que este enfoque puede traer:

- Cross-platform: Desarrollar y probar en múltiples plataformas asegura que el software funcione correctamente para una amplia base de usuarios. "Write once, run anywhere" es un objetivo importante para muchas aplicaciones y, aunque de base los lenguajes aseguran que esto pueda ser cierto, cada programador pone de su parte para que no lo sea.
- Flexibilidad: Muchas empresas utilizan entornos mixtos y la capacidad de adaptarse es una ventaja competitiva.
- Comprensión de las diferencias: Trabajar en diferentes sistemas ayuda a comprender mejor las peculiaridades de cada uno, mejorando la capacidad de depuración y optimización.

En lugar de aferrarse dogmáticamente a un solo sistema operativo, un enfoque más productivo es elegir la herramienta adecuada para el trabajo adecuado, manteniendo la flexibilidad de moverse entre diferentes plataformas cuando sea necesario.

### 4. El depurador es para los débiles

Desmintamos una idea

```text
Un "verdadero programador" escribe código perfecto al primer intento
```

Esta historia circula en el mundo de la programación desde hace años. Más o menos todos los programadores famosos se han cosido esta imagen, y cada uno de nosotros está listo para contarla al final de la noche cuando las cervezas ya se han acabado.
La realidad es que la depuración y las pruebas son una parte esencial e inevitable del proceso de desarrollo de software y esta mentalidad de resistencia al uso de herramientas de depuración, viéndolas como una especie de "muleta", es algo que debe superarse.

Ya no cuento las veces que he tomado un software considerado "concluido", lleno de pruebas funcionales, y poco a poco han surgido problemas, casos de uso no cubiertos, problemas de análisis y diseño: no, la ilusión de que la primera versión de un programa sea capaz de generar un software perfecto y que las pruebas sean suficientes para entender qué funciona o no funciona es solo una ilusión.

En estas situaciones: logs, depuración y nuevas pruebas se vuelven necesarios para entender qué no funciona y cómo resolverlo.

### 5. El código está todo en mi cabeza

El análisis, la compartición del conocimiento y la documentación son aspectos a menudo descuidados en la programación.

```text
Lo tengo todo en la cabeza
```

No existe una frase menos productiva que esta, que atrofia cualquier tipo de discusión y colaboración.

Existe una narrativa romántica del programador como genio solitario, capaz de mantener sistemas complejos enteros en su mente y de ver su software como Neo veía Matrix.
Este enfoque tiene un error de base: la mente humana, aunque maravillosa, tiene límites en la cantidad de información que puede mantener.

No todos somos Dennis Nedry, el programador de Jurassic Park que sabía todo el código del parque de memoria y, aunque lo fuéramos, recordemos qué le pasó.

Olvidar el pasado es una forma de protección que activa nuestro cerebro para evitar volverse loco. Este es el motivo por el cual es importante documentar el código, compartir el conocimiento y trabajar en equipo.

Pero incluso si la propia mente tuviera una capacidad infinita, hay otros motivos por los cuales el "código en mi cabeza" es un problema:

- Colaboración: Si el funcionamiento del código es claro solo en la mente de quien lo escribió, se vuelve difícil para otros contribuir o mantener el proyecto.
- Propensión a errores: Sin una documentación clara o comentarios en el código, es fácil olvidar detalles importantes o hacer suposiciones erróneas.
- Onboarding complicado: Los nuevos miembros del equipo tendrán dificultades para comprender y contribuir al proyecto.

Es necesario que el "celodurista" se dé cuenta de que el código es un producto colaborativo y no compartir información no es el mejor enfoque para mantener su trabajo, sino la mejor manera de perderlo.

Animemos a estos programadores a documentar, escribir wikis, hacer revisiones de código, usar diagramas y esquemas, para compartir el conocimiento.

Un enfoque que valore la documentación y la compartición del conocimiento no solo hace el proyecto más robusto y mantenible, sino que también contribuye al crecimiento profesional de todo el equipo.

### 6. Los programadores no usan ChatGPT

Seamos sinceros: las inteligencias artificiales son todo, menos inteligentes.

```text
Mira cuántos errores comete ChatGPT, no puede reemplazar a un programador
```

Las alucinaciones, pero sobre todo el uso incorrecto y superficial de las IA, llevan a muchos programadores a pensar que son herramientas inutilizables.
No, las IA no son motores de búsqueda, son herramientas de agregación lingüística, que pueden aprender nuestro contexto de trabajo, y como tales deben ser usadas.

A estas teorías se superponen cada vez más las teorías de que en el futuro las IA reemplazarán a los programadores.
El programador "duro y puro" no usa estos instrumentos, porque no los necesita, porque no funcionan, porque "yo soy mejor".

Todo cierto, pero solo en parte. La realidad es que las IA son herramientas que pueden ayudar a los programadores a escribir código más rápido y con menos errores, pero no basta una hora para llegar a este resultado, se necesitan semanas de uso para entender mejor cómo usar esta herramienta e identificar rápidamente sus pros y contras.

La IA debe ser vista como una herramienta de potenciación, como la evolución del autocompletado de los IDE modernos, pero capaz de extender el completado a un contexto más amplio y complejo.

Recientemente vi la película Atlas, no por Jennifer Lopez, como muchos de vosotros estaréis propensos a pensar, sino para enriquecer mi mente con nuevas imágenes sobre futuros posibles. Dentro de esta película, la IA se ve como un complemento del trabajo del hombre y ambos se mejoran y potencian, trabajando en simbiosis.

Para quienes pasaron las tardes de su infancia viendo Star Trek: es la evolución de la fusión mental de los vulcanianos o del simbionte de los Trill.

Hay muchos aspectos de la vida de un programador que se benefician de una IA:

- Generación de boilerplate: La IA puede producir rápidamente estructuras de código básicas, permitiendo a los programadores concentrarse en los aspectos más complejos y creativos.
- Depuración asistida: Modelos como ChatGPT pueden ayudar a identificar errores en el código y sugerir posibles soluciones.
- Exploración de nuevas tecnologías: La IA puede proporcionar explicaciones y ejemplos de uso para frameworks o bibliotecas con las que el programador no está familiarizado.
- Optimización: Sugerencias para mejorar la eficiencia o la legibilidad del código.
- Pruebas: Generación de pruebas automáticas para verificar el correcto funcionamiento de su trabajo.

En lugar de rechazar categóricamente el uso de las IA, los programadores deberían considerarlas como herramientas que pueden mejorar su productividad y la calidad de su trabajo.

## Conclusión

El "celodurismo" en la programación, aunque arraigado en la historia como símbolo de ingenio y optimización, corre el riesgo de convertirse en un freno a la innovación y la eficiencia en el mundo del desarrollo de software moderno.

Un enfoque más equilibrado reconoce el valor de la tradición y la experiencia, pero permanece abierto a las nuevas tecnologías y metodologías que pueden mejorar el proceso de desarrollo.

El verdadero signo de un programador experimentado no es la adhesión dogmática a prácticas del pasado, sino la capacidad de evaluar críticamente y adoptar las herramientas y prácticas más adecuadas para cada situación específica.

Admiro a los celoduristas por su tenacidad, pero estoy seguro de que si tuvieran más coraje podrían obtener grandes beneficios de una reevaluación de sus posiciones.

