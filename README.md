![](RackMultipart20201027-4-1lm0f6e_html_2747e5c0c46cc46f.gif)

# Primer Laboratiorio teoria de lenguajes

Compilador Léxico Gráfico Básico para Lenguaje Dart

![](RackMultipart20201027-4-1lm0f6e_html_3d7e6bf4c0671732.gif)

Universidad De Antioquia.

Teoría de Lenguajes y Laboratorio

 ![](RackMultipart20201027-4-1lm0f6e_html_6bd0f676fdae0e42.gif)

# Contenido

[Lenguaje Seleccionado y metodología para codificar: 1](#_Toc54513847)

[Sintaxis Dart y Estructuras a Analizar. 2](#_Toc54513848)

[Estructura Variable. 2](#_Toc54513849)

[Constante: 3](#_Toc54513850)

[Tipo 6](#_Toc54513851)

[Separadores 6](#_Toc54513852)

[Operadores 7](#_Toc54513853)

[Autómata Finito. 7](#_Toc54513854)

[Detalle de Implementación 11](#_Toc54513855)

# Lenguaje Seleccionado y metodología para codificar:

El Lenguaje seleccionado para el análisis léxico grafico es Dart, Dart es un lenguaje de programación desarrollado por Google en el año 2011 como una alternativa moderna a JavaScript para la programación web, últimamente ha cobrado mucha importancia debido a que sobre dart se lanzó un framework enfocado en la interfaz de usuario para desarrollo de aplicaciones nativas en cualquier sistema llamado flutter.

En cuanto a la metodología para codificar primero es necesario aclarar que, aunque el compilador analiza código Dart no será programado en este mismo lenguaje, en su lugar se optó por el lenguaje Python en su versión 3+ y para la interfaz de usuario se utiliza el módulo Tkinter de Python.

- El primer paso para la construcción será definir unos AFND con transiciones lambda para cada estructura a analizar.
- Estos autómatas se convertirán en expresiones regulares aceptadas por lenguaje Python con las cuales se detectarán los símbolos que componen el autómata.
- Las expresiones regulares también serán utilizadas para determinar las clases solicitadas en la lista ligada.
- Se hará un AFD para los símbolos ingresados
- Se simplificará el autómata finito.
- Se implementará un autómata de pila para revisar si los paréntesis están balanceados.
- Para llevar todo a código se tendrá una arquitectura de tres capas:
  - Vista: main-gui.py
  - Controlador: analizador\_lexico.py
  - Modelo: automata.py , lista\_ligada.py

# Sintaxis Dart y Estructuras a Analizar.

Dart posee una sintaxis al estilo de lenguajes como C, los nombres de constantes y variables no pueden contener espacios, ni símbolos matemáticos, flechas, o caracteres Unicode.

Reglas.

- El nombre de variable puede ser mínimo una letra o puede tener .
- Palabras reservadas no están permitidas
- Espacios en blanco no están permitidos
- El primer carácter siempre debe ser una letra y no un digito
- El nombre de la variable es &quot;case sensitive&quot;
- Los caracteres especiales están prohibidos con excepción del guion al piso (\_) y el símbolo cash ($)

Nota: el carácter especial cash ($) es valido solo en la interpolación de cadenas (String Interpolation), esto sale del alcance y no será implementado.

Un ejemplo de la sintaxis Dart la podemos tomar de su sitio web:

// Define a function.

void printInteger(int aNumber){

print(&#39;The number is $aNumber.&#39;);// Print to console.

}

// This is where the app starts executing.

void main(){

var number =42;// Declare and initialize a variable.

printInteger(number);// Call a function.

}

## Estructura Variable.

Se necesita que el compilador permita la creación y o definición de variables, para lo cual se implementa la siguiente expresión regular que nos permita obtener los símbolos que son variables.

Sea a-z cualquier letra del abecedario minúscula, y sea A-Z cualquier letra del abecedario en mayúscula, si queremos encontrar cualquier secuencia que detecte al menos una o más letras mayúsculas o minúsculas tenemos el siguiente autómata:

![](RackMultipart20201027-4-1lm0f6e_html_2ad3a36826bb2087.gif)

Si luego pensamos en el hecho que 0-9 representa cualquier número del cero al nueve y que el guion al piso (\_) se representa a si mismo. Y luego queremos buscar una en la forma básica para que reciba cero o más veces una secuencia a-zA-Z0-9\_ es decir una expresión regular de la forma:

**AF -\&gt; (**a-zA-Z0-9\_**)****\***

![](RackMultipart20201027-4-1lm0f6e_html_f6b6125d5dcaaef3.gif)

Si luego pensamos que el autómata requerido debe evaluar al menos una de la primera secuencia**(**a-zA-Z**)****+ **y después una o ninguna de la segunda secuencia** ( **a-zA-Z0-9\_** ) ****\*** , entonces podemos utilizar el operador de concatenación para obtener el siguiente autómata

![](RackMultipart20201027-4-1lm0f6e_html_5e4bef248221b69.gif)

Al final la regex Python que equivale a este automata es AF-\&gt; ^[a-zA-Z][a-zA-Z0-9\_]\*$

## Constante:

Una constante en Dart puede ser de tipo numérico o de tipo de texto.

Para un tipo numérico se necesita que empiece o no por un solo símbolo + o –

![](RackMultipart20201027-4-1lm0f6e_html_942c5bded7b90f74.gif)

seguido por cero o cualquier cantidad de dígitos.

![](RackMultipart20201027-4-1lm0f6e_html_844920a4bcf14d76.gif)

uno o ningún punto

![](RackMultipart20201027-4-1lm0f6e_html_7434ca053bf16804.gif)

y cualquier cantidad de dígitos nuevamente, (como se representó con el autómata de arriba), y una o ninguna vez la letra &quot;e&quot;

![](RackMultipart20201027-4-1lm0f6e_html_d1e90599293fe823.gif)

Seguida uno o ningún símbolo +- , (automat descrito arriba) y termine obligatoriamente digito

![](RackMultipart20201027-4-1lm0f6e_html_3e0554dedbc1d4e1.gif)

La exprsion para esta regex es ^[+-]?[0-9]\*[.]?[0-9]\*[e]?[+-]?[0-9]$ que se representa por el siguiente automata.

![](RackMultipart20201027-4-1lm0f6e_html_e6c00cef97394cba.gif)

O utilizando una notación simplificada por el siguiente:

![](RackMultipart20201027-4-1lm0f6e_html_7049b9b39d2f7b48.gif)

Para un tipo texto solamente se necesita que empiece y termine encerrado entre comillas

^\&quot;.\*\&quot;$

Realizando la unión de las constantes numéricas y las constantes de texto nuestra expresión regular quedaría de la siguiente forma.

(^[+-]?[0-9]\*[.]?[0-9]\*[e]?[+-]?[0-9]$|^\&quot;.\*\&quot;$)

## Tipo

Para declarar el tipo de las variables Dart utiliza lo que ellos llaman un tipo inferido, esto quiere decir que la variable se le puede asignar alguno de los tipos bool, String, num, int o double; o se puede designar con la palabra var en cuyo caso dart se va a encargar de asignarle un tipo y encargarse que lo conserve hasta el final de la ejecución.

![](RackMultipart20201027-4-1lm0f6e_html_cbc2e54d666ecd46.gif)

El grafico anterior muestra un autómata finito que admite o solo las palabras utilizadas para instanciar una variable o la secuencia nula AF -\&gt;(bool |String |num |int |double |var )\* esto es porque un nombre de una variable puede o no estar precedido por la declaración de su tipo.

## Separadores

Los separadores en dart son la coma (,) , el punto y coma (;), paréntesis de apertura o cierre ( &quot;(&quot; ó &quot;)&quot;), llaves (&quot;{&quot; ó &quot;}&quot;) y corchetes(&quot;[&quot; ò &quot;]&quot;)

![](RackMultipart20201027-4-1lm0f6e_html_30c1517d81ab18c8.gif)

En este caso la expresión regular y el autómata no admiten ni la secuencia nula ni tampoco admiten más de un separador puesto que sería considerado aparte. \(|\)|\[|\]|\{|\}|,|;

## Operadores

Dart utiliza una gran cantidad de operadores, expondremos todos, pero al final se seleccionaron solo algunos (que se resaltan en verde), para reducir el tamaño del autómata y de la expresión regular.

Aritméticos:

| + | - | \* | / | % | ~/ |
| --- | --- | --- | --- | --- | --- |

Lógicos:

| &amp;&amp; | || |
| --- | --- |

 Comparación

| == | != | \&gt;= | \&gt; | \&lt;= | \&lt; |
| --- | --- | --- | --- | --- | --- |

Asignación

| = | \*= | /= | ~/= | %= | += | -= | \&lt;\&lt;= | \&gt;\&gt;= | &amp;= | ^= | |= |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

![](RackMultipart20201027-4-1lm0f6e_html_6305e5a96092d2b.gif)

## Autómata Finito.

Para el reconocimiento de la estructura del lenguaje se utilizo una aproximación de un AFD del cual se muestra su representación gráfica y las tablas de transición.

![](RackMultipart20201027-4-1lm0f6e_html_f52edb56678966aa.gif)

Las tablas de transición son las siguientes:

AFD:

Símbolos de Entrada = {Tipo, Coma, Igual, Boleano, Variable, Constante Separador, Operador Mat, Asignacion, Operador Logico, Punto y Coma}

Estados = {00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ERR}

Inicial = {00}

Aceptación = {07, 00}

Tabla de Transición:

![](RackMultipart20201027-4-1lm0f6e_html_1fabb6f53e8c6b43.jpg)

Se observa que el automata tiene varios estados que son iguales como el 00 con el 07 y el estado 10 que es igual al 11, por lo tanto realizamos un proceso de particionar estos estados, del cual nos quedan estas particiones finales.

![](RackMultipart20201027-4-1lm0f6e_html_b93cd4f628841e44.jpg)

![](RackMultipart20201027-4-1lm0f6e_html_bb59bfcb80013c51.jpg)

![](RackMultipart20201027-4-1lm0f6e_html_26d2c829cc28e8d0.jpg)

![](RackMultipart20201027-4-1lm0f6e_html_aee9cc2af2357f62.jpg)

![](RackMultipart20201027-4-1lm0f6e_html_640e21ccd5a895fd.jpg)

![](RackMultipart20201027-4-1lm0f6e_html_ae3961935feeb6d5.jpg)

![](RackMultipart20201027-4-1lm0f6e_html_c9b9446c5103e54a.jpg)

![](RackMultipart20201027-4-1lm0f6e_html_c8f98350c9365e44.jpg)

![](RackMultipart20201027-4-1lm0f6e_html_b823c60c713a2ba5.jpg)

![](RackMultipart20201027-4-1lm0f6e_html_801dea99b3cd3207.jpg)

![](RackMultipart20201027-4-1lm0f6e_html_4daab5be2f8c310b.jpg)

![](RackMultipart20201027-4-1lm0f6e_html_4316a9c50cb968c7.jpg)

Luego se hace un nuevo autómata desde la partición inicial para eliminar los estados extraños lo que nos queda de la siguiente manera.

![](RackMultipart20201027-4-1lm0f6e_html_9ab886db76215314.jpg)

Para la detección del balanceo de los paréntesis se utilizo el siguiente autómata de pila visto en clase:

Símbolos de entrada = { (, ), ┤}

Símbolos en la Pila = { (, ▼}

Estados = {}

Configuración inicial de la pila = ▼

Transiciones:

|
 | ( | ) | ┤ |
| --- | --- | --- | --- |
| ( | #1 | #2 | R |
| ▼ | #1 | R | A |

Estado #1: Apile (&quot;(&quot;), permanezca en el estado, Avance.

Estado #2: Des Apile, permanezca en el estado, Avance.

R: Rechace.

A: Acepte.

# Detalle de Implementación

Para llevar este autómata a código Python se implementa la case Autómata que tiene un método establecer estado según el símbolo y de revisar el balance de paréntesis, también se encarga de enviar los mensajes de error al archivo de log.

Esta clase será llamada por la clase AnalizadorLexico que se encarga de separar el texto completo en cada una de sus líneas y luego se encarga de separar cada línea en la mínima unidad para eso va a utilizar unos caracteres que servirán como separadores, estos son el espacio, la coma, el punto y coma, los paréntesis y los operadores.

Luego de esto el AnalizadorLexico va a llevar estos tokens a una lista ligada de la clase ListaLigada que será la encargada de dar solución a la representación solicitada en el otrosí del trabajo; ListaLigada recibirá objetos del tipo Nodo que son capaces de revisar si el dato que tienen almacenado pertenece a una de las clases solicitadas en el otrosí o no y también si ese mismo dato es uno de los símbolos que va a reconocer el autómata en lenguaje Dart, al final de una línea se va a escribir su representación como lista ligada en el archivo de log.

La clase AnalizadorLexico será llamada desde una clase GUI esta clase tendrá todos los elementos de la interfaz gráfica de usuario y se encargara de cargar los archivos de texto para mostrarlos en uno de sus cuadros de texto situado a la izquierda, y también cuando se termine el análisis del texto va a consultar el archivo de logs y mostrarlo en el cuadro de texto situado en la derecha, cada vez que se cargue un nuevo archivo ambos cuadros se van a borrar.

En general la arquitectura propuesta para este programa se basa en el patron MVC aunque se debe admitir que la clase GUI posee un nivel de acoplamiento puesto que tiene funciones tanto de la vista como del controlador, se considera que separar estas funciones en dos clases por el momento solo agrega complejidad al programa debido a que tanto la vista como el controlador tienen actualmente muy pocos métodos. Respecto al diseño no ha utilizado por el momento ningún patron, aunque posiblemente se agregue en el futuro un Observer del estado del autómata. siguiente diagrama de clases resume la arquitectura y el diseño de la aplicación:

![](RackMultipart20201027-4-1lm0f6e_html_1ae14583565e6c74.gif)

# Manual de Usuario.

## Repositorio:

El programa se encuentra alojado en el repositorio de github [https://github.com/johnymarin/TL\_LexicoGraph](https://github.com/johnymarin/TL_LexicoGraph)

## Requerimientos:

Para ejecutar esta primera entrega solo es necesario tener instalado Python en la version 3.6 o superior, todos los módulos utilizados hasta el momento hacen parte del lenguaje Python para estas versiones, se enumeran los imports solo en caso de algún problema.

- re
- logging
- collections
- tkinter
- shlex
- io

el repositorio cuenta con un archivo requirements.txt que contiene todos los requerimientos hasta ahora.

Para ejecutar el programa puede hacerse desde cualquier IDE ejecutando el archivo main.py como se muestra en esta imagen de pycharm:

![](RackMultipart20201027-4-1lm0f6e_html_2df1d1b375307515.png)

Al ejecutar el script de Python se abre la siguiente ventana de tkinter

![](RackMultipart20201027-4-1lm0f6e_html_e0aeaabff72bf89e.png)

Se observan espacios de texto y un botón &quot;Abrir&quot; en la esquina izquierda superior, al dar click en este se abre un selector de archivos donde se debe tener un código en el lenguaje Dart.

![](RackMultipart20201027-4-1lm0f6e_html_e270f0717d634770.png)

Al abrir un archivo el programa procederá a mostrar el texto del archivo en el cuadro de texto de la izquierda y los resultados en la derecha, estos resultados se componen de la línea a analizar, la representación como lista ligada y los errores ya sean en el código o en el balanceo de paréntesis en caso de existir

![](RackMultipart20201027-4-1lm0f6e_html_b4daf65e38543598.png)

La ventana sigue abierta para que el usuario analize otro archivo o cierre desde el botón cerrar de su sistema operativo.