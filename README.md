<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<div align="center">

# Ft_trascendence


[![GitHub último commit](https://img.shields.io/github/last-commit/andresmejiaro/transcend?color=blue&label=Último%20commit&logo=git&maxAge=3600)](https://github.com/andresmejiaro/transcend/commits)
[![GitHub forks](https://img.shields.io/github/forks/andresmejiaro/transcend?label=Forks&color=blue&maxAge=3600)](https://github.com/andresmejiaro/transcend/network)

[![GitHub tamaño del código en bytes](https://img.shields.io/github/languages/code-size/andresmejiaro/transcend?label=Tamaño%20del%20código&maxAge=3600)](https://github.com/andresmejiaro/transcend)


[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/MatPizzolo/ft_transcendence/blob/main/README.en.md)

</div>


## PIXEL PONG

<div align="center"">
  Bienvenido a nuestro sitio web SPA, donde los usuarios participan en partidas en tiempo real contra otros jugadores o desafían a la IA inteligente para juego en solitario. El proyecto está dedicado a ofrecer una interfaz de usuario fluida y visualmente cautivadora, mejorando la experiencia de juego para todos.
</div>

</br>
</br>

## Índice de Contenidos

- [Web](#web)
- [Características](#características)
- [Tecnologías](#tecnologías)
- [Juego](#juego)
- [Arquitectura](#arquitectura)
- [Conceptos](#conceptos)

</br>
</br>

## Web

![Menús_del_juego](https://github.com/MatPizzolo/ft_transcendence/blob/main/readme-tools/trascend-whole-vid.gif)


</br>
</br>

## Características

- **Pong Multijugador en Tiempo Real:** Participa en emocionantes partidas de Pong con amigos u otros jugadores en línea en un entorno multijugador en tiempo real.

- **Juega Contra IA:** Una IA funcional para darte la oportunidad de mejorar tu juego para impresionar a tus amigos.

- **Autenticación:** Implementación de Autenticación de Usuario Estándar y OAuth 42 intra

- **Amigos:** Los usuarios pueden agregar a otros usuarios como amigos y ver su estado (en línea, desconectado, en una partida)

- **Historial de Partidas:** Los usuarios pueden ver su historial de partidas y buscar estadísticas de otros usuarios.

- **Tabla de Clasificación:** Los usuarios suben y bajan en el ranking después de cada victoria/derrota

- **Torneos:** Los usuarios pueden crear y unirse a torneos

</br>
</br>

## Tecnologías

#### Front End
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

#### Back End
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

#### DevOps
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
Makefile

</br>
</br>

## Juego

Es crucial que el juego tenga funcionalidad del lado del servidor como fuente autoritativa de verdad y control. Esto asegura un entorno de juego seguro y justo al prevenir la manipulación no autorizada o el engaño en el lado del cliente. Sin embargo, el reconocimiento de problemas de latencia impulsa la incorporación de capacidades front-end con JavaScript. Este enfoque dual permite una experiencia de usuario receptiva y agradable, donde el front-end puede manejar ciertos aspectos del juego en tiempo real, minimizando el impacto de la latencia en las interacciones del jugador.

Este balance entre la robustez del lado del servidor y la capacidad de respuesta del front-end contribuye a una experiencia de juego óptima e inclusiva para todos los usuarios.

</br>
</br>

## Arquitectura

### Visión General de la Estructura del Proyecto

El proyecto comprende varias carpetas y archivos, cada uno con un propósito distinto:

![Arquitectura de Trascendence](https://github.com/andresmejiaro/transcend/blob/readme_documentation/attach-files/Arquitecture_trascendence.png)

La estructura del proyecto segrega funcionalidades y componentes, dividiéndolos en backend, frontend, pruebas, implementación de IA y configuraciones. Cada directorio contiene actualizaciones y funcionalidades específicas basadas en commits recientes, con el objetivo de mejorar la experiencia general del usuario, la lógica del servidor y las funcionalidades del juego.

- **Backend:** Maneja la lógica y funcionalidades del lado del servidor. Las actualizaciones recientes incluyen mejoras relacionadas con el WebSocket del lobby y el estado en línea. Usando como imagen base `python:3.7-alpine` y expone el puerto 8000 para permitir la comunicación del backend.
  
  El archivo `settings.py` determina el comportamiento particular del servidor, entornos Dockerizados, gestión de aplicaciones, base de datos, la utilización de canales para comunicación en tiempo real y CORS para permitir peticiones entre diferentes orígenes.

  El archivo `urls.py` gestiona el enrutamiento de URL mapeando URLs específicas a las vistas o endpoints correspondientes dentro del servidor Django. Configura el panel de administración, endpoints de API, URLs de WebSocket y sirve archivos multimedia estáticos.

  El script `manage.py` es la herramienta de línea de comandos de Django utilizada para tareas administrativas. Configura el entorno Django, ejecuta comandos de gestión y sirve como punto de entrada para interactuar con el proyecto Django a través de la línea de comandos.

- **Frontend:** Las Aplicaciones de Página Única (SPAs) operan actualizando dinámicamente el contenido en una única página web sin requerir recargas completas. Utilizan JavaScript para obtener datos del servidor, actualizar el DOM y gestionar las interacciones del usuario sin problemas.

- **Nginx:** Incluye configuraciones y actualizaciones relacionadas con el servidor web NGINX, particularmente en la fusión de la rama de desarrollo.

- **Python-pong:** Este código Python implementa un juego Pong usando la biblioteca curses para la Interfaz de Línea de Comandos (CLI).

- **APItests:** Contiene clientes CLI para pruebas de API, principalmente enfocados en el juego CLI.

## Conceptos

Bibliotecas instaladas en el Backend Django:

asgiref==3.7.2

asttokens==2.4.1

async-timeout==4.0.3

channels==4.0.0

channels-redis==4.1.0

colorama==0.4.6

Django==3.2.23

django-cors-headers==4.1.0

executing==2.0.1

icecream==2.1.3

importlib-metadata==6.7.0

msgpack==1.0.5

passlib==1.7.4

Pillow==9.5.0

psycopg2-binary==2.9.9

Pygments==2.17.2

pyotp==2.9.0

pypng==0.20220715.0

pytz==2023.3.post1

qrcode==7.4.2

redis==5.0.1

six==1.16.0

sqlparse==0.4.4

typing_extensions==4.7.1

zipp==3.15.0



</br>
</br>
