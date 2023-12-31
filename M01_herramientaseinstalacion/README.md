# Instalación de Herramientas


#### Preparando tu computadora
Antes de comenzar deberás descargar en tu computadora las siguientes herramientas de trabajo:
1. Editor de texto
2. Git
3. Github
4. Python

Luego deberás realizar la clonación del. Te explico cómo hacerlo en el tutorial: https://youtu.be/nxu3EZVzP8I 

> **Importante**: Github cambió el método de autenticación, ahora es por PAT (Personal Access Token), para crearlo pueden seguir este [link](https://docs.github.com/es/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). Pueden elegir expiration infinita para hacerlo una sóla vez.

## Editores de Texto

Para poder escribir código que pueda ser interpretado por un lenguaje de programación, necesitamos utilizar un editor de texto.

## Visual Studio Code

Es un editor desarrollado por Microsoft.

Tiene integrado el control de versiones mediante Git y Github para tener un seguimiento de tus proyectos. Brinda una cantidad de extensiones que facilitan el trabajo de un desarrollador.

Para descargarlo, nos dirigimos al sitio oficial, en la sección Download y descargamos el instalador según nuestro Sistema Operativo:

<https://code.visualstudio.com/download>

Una vez finalizada la descarga, procedemos a ejecutar el instalador.

## Git

### ¿Qué es Git?

Git es un sistema de control de versiones, distribuido y open source. Un control de versiones es un sistema que registra los cambios realizados en un archivo o conjunto de archivos a lo largo del tiempo, de modo que puedas recuperar versiones específicas más adelante.

### Instalación

#### Para Mac y Linux

Ver estos enlaces:

<https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git>

<https://www.youtube.com/watch?v=PSULlxUk744>

<https://www.youtube.com/watch?v=oV0spTF71AI>

#### Para Windows

Ingreso a <https://git-scm.com> y descarga la última versión.

Una vez descargado, se abre el archivo .exe

Clickeamos “Next”

En este momento de la instalación, si quieren, pueden elegir el editor de texto que van a usar. (Importante, ténganlo instalado antes de instalar Git)

Seguimos clickeando “Next” y luego “Install"

Por último, ¡finalizar! Si seleccionan la opción "Launch Git Bash", una vez que finalizan la instalación se va a abrir la consola

Otra forma de abrir la consola es haciendo click derecho sobre el escritorio y elegir la opción "Git Bash Here"

Una vez instalado Git van a poder visualizar la consola: ingresamos el comando `git --version` para chequear que está instalado. Si ven la consola así, ya están listos para comenzar a trabajar!


## GitHub

### ¿Qué es GitHub?

Es una red para almacenar tus repositorios, sería un repositorio de repositorios. Es uno de los tantos disponibles en internet, y el más popular. GitHub **NO** es lo mismo que Git, aunque funcionen muy bien juntos. Github es un lugar donde podés compartir tu código o encontrar otros proyectos. También actúa como portfolio para cualquier código en el que hayas trabajado.

### Comenzando

1. Para comenzar nos creamos una cuenta --- > <https://github.com> 🚀

2. Una vez registrados, ingresamos con usuario y contraseña

3. Listo! Ahora vemos una página de inicio

A la izquierda tenemos un acceso rápido a **mis repositorios**.

En el centro vemos la actividad de los usuarios a quienes seguimos.

En la parte superior derecha, vemos nuestra imagen de perfil. Desde ahí podemos desplegar opciones para gestionar nuestro perfil, repositorios y configuración.

Podemos poner una foto de perfil, editar el nombre, agregar la ubicación, link y organizaciones a las que pertenecemos. En el centro podemos fijar los repositorios que queremos mostrar para que estén visibles en nuestro perfil.

Más abajo se muestra un diagrama de todas las contribuciones que vamos haciendo a los repositorios.

Si accedemos a la pestaña de arriba que dice `repositorios` veremos una lista de todos ellos.

Así se ve un repositorio. Arriba a la izquierda tenemos el `nombre de usuario/nombre del repo`.

En el centro podemos ver todos los archivos que tiene dentro el repo. El botón verde que dice `Code` es importante, si clickeamos ahí vamos a poder obtener la url del repo, para así poder **_clonarlo_** (esto lo veremos más adelante).

Arriba a la derecha encontramos tres botones. `Watch` nos permite seguir un repositorio, mientras que con `Star` podemos marcar como favorito un repo que nos guste. Por último tenemos `Fork`, este es **muy** importante.

Ya tenemos todo para empezar... Éxitos!!! 🍀

## Python

### ¿Qué es Python?

Es un lenguaje de programación sencillo de leer y escribir debido a su alta similitud con el lenguaje humano. Además, se trata de un lenguaje multiplataforma de código abierto y, por lo tanto, gratuito, lo que permite desarrollar software sin límites

### Instalación 

Si estás usando Windows:

Elige una versión 3.10
1. Para obtener el instalador dirígete a [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Descarga el instalador y ejecútalo en tu computadora.
3. Habilita la casilla de verificación en Install launcher for all users y Add Python 3.8 to PATH. A continuación presiona en Install Now. Windows te solicitará permisos para instalar Python en tu computadora.
4. Al finalizar la instalación se abrirá una ventana, en ella deberás presionar en la opción Disable path length limit. Windows te solicitará permisos para realizar este cambio.

Si estás usando Mac:

Mac OS X suele tener python instalado por defecto. Para verificarlo abrí la terminal, en el buscador de tu Mac, y escribí Python. Comprobar que está correctamente instalado: 

```bash
Python
Python 2.7.13 (default, Mar 25 2021, 18:52:10) 
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Si no te figura o queres descargar la última versión dirígete a: [https://es.wikibooks.org/wiki/Python/Instalaci%C3%B3n_de_Python/Python_en_Mac_OS_X](https://es.wikibooks.org/wiki/Python/Instalaci%C3%B3n_de_Python/Python_en_Mac_OS_X)

Si estás usando Linux:

En una distribución estándar Linux dispone por defecto el intérprete Python instalado, para comprobar la correcta instalación solamente debería ejecutar el comando en la consola:

```bash
python
Python 2.7.13 (default, Sep 26 2018, 18:42:22)
[GCC 6.3.0 20170516] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Si le muestra los mensajes anteriores está correctamente instalado el intérprete Python en su Linux.

Si al ejecutar el comando anterior muestra el mensaje:

```bash
python
bash: python: no se encontró la orden
```

Esto es debido a que no tiene instalado el intérprete, así que debe ejecutar el siguiente comando:
```bash
sudo apt-get install -y python-dev
```

De nuevo vuelva a ejecutar en su consola de comando el comando python. Ya están listos para comenzar a trabajar

