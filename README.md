<div align="center">

# Ft_trascendence


[![GitHub last commit](https://img.shields.io/github/last-commit/andresmejiaro/transcend?color=blue&label=Last%20commit&logo=git&maxAge=3600)](https://github.com/andresmejiaro/transcend/commits)
[![GitHub forks](https://img.shields.io/github/forks/andresmejiaro/transcend?label=Forks&color=blue&maxAge=3600)](https://github.com/andresmejiaro/transcend/network)

[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/andresmejiaro/transcend?label=Code%20size&maxAge=3600)](https://github.com/andresmejiaro/transcend)

</div>


## PIXEL PONG

<div align="center"">
  Welcome to our SPA website, where users engage in real-time matches against fellow players or challenge the intelligent AI for solo play. The project is dedicated to delivering a seamless and visually captivating user interface, enhancing the gaming experience for everyone. 
</div>

</br>
</br>

## Table of Contents

- [Web](#web)
- [Stack](#stack)
- [Game](#game)
- [Arquitecture](#arquitecture)
- [Features](#features)
- [Concepts](#concepts)

</br>
</br>

## Web

![Game_menus](https://github.com/MatPizzolo/ft_transcendence/blob/main/readme-tools/trascend-whole-vid.gif)


</br>
</br>

## Stack

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


## Game

It is crucial for the game to have server-side functionality as the authoritative source of truth and control. This ensures a secure and fair gaming environment by preventing unauthorized manipulation or cheating on the client side. However, the acknowledgment of latency issues prompts the incorporation of front-end capabilities with JavaScript. This dual approach allows for a responsive and enjoyable user experience, where the front end can handle certain aspects of the game in real-time, minimizing the impact of latency on player interactions.

This balance between server-side robustness and front-end responsiveness contributes to an optimal and inclusive gaming experience for all users.

</br>
</br>



## Arquitecture

### Project Structure Overview

The project comprises various folders and files, each serving a distinct purpose:

![Arquitectura de Trascendence](https://github.com/andresmejiaro/transcend/blob/readme_documentation/attach-files/Arquitecture_trascendence.png)

The project structure segregates functionalities and components, dividing them into backend, frontend, testing, AI implementation, and configurations. Each directory contains specific updates and functionalities based on recent commits, aiming to enhance the overall user experience, server logic, and game functionalities.

- **Backend:** Handles the server-side logic and functionalities. Recent updates include enhancements related to lobby WebSocket and online status. Using as image base `python:3.7-alpine` and exposes de port 8000 to allow backend communication.
  
  The `settings.py` file determine the server's particular behavior, Dockerized environments, application management, database, the utilization of channels for real-time communication, and CORS to enable requests between different origins.
Entails specific decisions regarding the server's implementation in a Dockerized environment, channel layers for asynchronous and real-time communication, and permitted origins for requests between domains.
  
  The `urls.py` file manages URL routing by mapping specific URLs to corresponding views or endpoints within the Django server. It configures the admin panel, API endpoints, WebSocket URLs, and serves static media files, controlling the handling of incoming requests in the web application.

  The `manage.py` script is Django's command-line tool used for administrative tasks. It configures the Django environment, executes management commands, and serves as the entry point for interacting with the Django project via the command line, facilitating tasks like database operations, server startup, and project management.

- **Frontend:** Single Page Applications (SPAs) operate by dynamically updating content on a single web page without requiring full page reloads. They utilize JavaScript to fetch data from the server, update the DOM, and manage user interactions seamlessly. Effective SPAs manage routing, allowing users to navigate within the app without causing full-page reloads, enhancing the user experience. Moreover, robust user authentication and identification play a pivotal role in SPAs, ensuring secure access to features, data, and resources. Proper authentication implementations enhance data security, privacy, and user trust by confirming the identity of individuals accessing the application, thereby safeguarding sensitive information and functionality.

- **Nginx:** Includes configurations and updates related to the NGINX web server, particularly in merging the develop branch.

  Within the Nginx configuration, settings for port 3000, typically used for Node.js applications or frontend services, might be established. Additionally, SSL/TLS configurations could be defined to ensure secure communication over HTTPS for enhanced data encryption and security measures. These SSL settings are crucial for encrypting data transmitted between clients and the server, particularly when dealing with sensitive information.

- **Python-pong:** This Python code implements a Pong game using the curses library for the Command Line Interface (CLI). It incorporates a primary loop allowing players to control paddles using designated keys. The code utilizes the curses module for the user interface, providing functionalities such as displaying the game screen and managing keyboard events for player control. Additionally, it enables interaction with a web server through HTTP requests and employs JSON files to record the game states at specific time intervals.

- **APItests:** Contains CLI clients for API testing, primarily focused on the CLI game.

  `CLItester.py` is a Python script responsible for managing WebSocket connections, handling game updates, and rendering a terminal-based Pong game. It enables communication with a WebSocket server, updates the game canvas based on incoming data, draws game components, and performs essential terminal actions such as screen clearing. Customizations or enhancements might be necessary depending on specific use cases.

  The `apitester.py` Python script is a utility tool designed for making HTTP requests to an API. It handles functionalities like obtaining CSRF tokens, signing up users, and executing various API calls (GET, POST, PUT, DELETE) using the requests library. The script supports CLI usage and requires proper endpoint specifications along with optional data for POST and PUT requests.

  The `wstester.py` Python script acts as a WebSocket client, allowing users to interact with a WebSocket server. It prompts for user input to specify the Tournament ID and Client ID, establishes a WebSocket connection to the provided URI, and enables users to send and receive messages in JSON format, facilitating communication with the WebSocket server through command inputs.

</br>
</br>



## Features

- **Real-time Multiplayer Pong:** Engage in exciting Pong matches with friends or other online players in a real-time multiplayer setup.

- **Play Against IA:** A working IA to  give you the oportunity to improve your gaming to impress your friends.

- **Authentication:** Standard User Authentication and OAuth 42 intra implementation
  
- **Friends:** Users can add other users as friends and see their status (online, offline, in a game)

- **Match History:** Users can see their and search for other uers match history and stats.

- **Leaderboard:** Users go up and down in ranking after each win/loss
  
- **Tournaments:** Users can create and join tournaments


</br>
</br>


## Concepts

Libraries installed in the Django Backend


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
