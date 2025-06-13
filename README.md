# rincon_republisher

Este proyecto es un ejemplo de integración en ROS 2 de nodos que usan **Action Server** y **Action Client**, con un sistema de lanzamiento completo.

## Descripción

- El nodo `republisher_server` actúa como **Action Server**.
    - Recibe un texto.
    - Envía como feedback cada palabra del texto a 1 Hz.
    - Al finalizar, indica que ha terminado.

- El nodo `republisher_client` actúa como **Action Client**.
    - Envía un texto como acción.
    - Recibe el feedback en tiempo real y lo muestra en la terminal.
    - Al finalizar, muestra `"Texto republicado!"`.

## Estructura

rincon_republisher/
├── rincon_republisher/ # Código fuente (server + client)
├── launch/republisher.launch.py # Launch file para ejecutar el sistema
├── resource/ # Archivo resource
├── setup.py # Configuración de instalación
├── package.xml # Metadata del paquete ROS2
└── republisher_interfaces/ # Mensaje custom Action

## Uso

###  Compilar el workspace

```bash
cd ~/ros2_rincon_ws
colcon build --symlink-install
source /opt/ros/jazzy/setup.bash
source ~/ros2_rincon_ws/install/setup.bash

###  Instalar el paquete en modo editable
```pip install --use-pep517 --break-system-packages -e ~/ros2_rincon_ws/src/rincon_republisher

###  Lanzar el sistema
```ros2 launch rincon_republisher republisher.launch.py text:="Hola mundo este es un ejemplo"

###  Esperado
El Action Client muestra feedback con cada palabra a 1 Hz.

Al final, muestra: "Texto republicado!".

###  Dependencias
ROS 2 Jazzy

rclpy

std_msgs

action_msgs
