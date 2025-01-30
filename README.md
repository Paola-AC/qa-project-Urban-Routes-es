# Paola Alfonso_Cohort 19

# Proyecto Urban Routes - Selenium 

# Proyecto de Pruebas Automatizadas - Urban Routes

## Objetivo

El objetivo de este proyecto es automatizar las pruebas del proceso de pedido de un taxi en la aplicación Urban Routes. El flujo cubre varias acciones, como la configuración de la dirección, la selección de la tarifa Comfort, el ingreso de información del usuario (número de teléfono, tarjeta de crédito, mensaje para el conductor), y la solicitud de productos adicionales como mantas y helados.

Las pruebas verificarán que todo el proceso se realice correctamente desde la configuración inicial hasta la búsqueda del taxi. Las pruebas están automatizadas usando Selenium y Pytest.

## Archivos del Proyecto

- **main.py**: Contiene las pruebas automatizadas que cubren todo el flujo de la aplicación Urban Routes.
- **Metodos.py**: Métodos que interactúan con la plataforma Urban Routes.
- **data.py**: Contiene datos sensibles y configuraciones del proyecto, como el número de tarjeta de crédito y la URL del servidor.
- **Codigo_phone.py**: Función que intercepta el código de confirmación para agregar una tarjeta de crédito.
- **requirements.txt**: Lista de dependencias del proyecto.
- **README.md**: Descripción del proyecto y guía de uso.
  
## Tecnologías y Técnicas Utilizadas

Este proyecto está basado en las siguientes tecnologías y herramientas:

- **Python**: Lenguaje de programación utilizado para escribir las pruebas automatizadas.
- **Selenium**: Herramienta de automatización para pruebas de aplicaciones web.
- **Pytest**: Framework para la ejecución de pruebas automatizadas en Python.
- **WebDriver**: Se utiliza para interactuar con el navegador (Chrome).
- **ChromeDriver**: Necesario para que Selenium interactúe con el navegador Google Chrome.
- **WebDriverWait** y **ExpectedConditions**: Para sincronizar la interacción con los elementos del DOM de la página, asegurando que estén listos antes de interactuar.
- **Keys**: Para simular presionar teclas como `TAB` y `ENTER` en el navegador.
  
## Como ejecutar las pruebas

1. Instalar las dependencias: Asegúrate de tener un entorno virtual configurado y activo. Instala las dependencias necesarias
2. Configurar la URL del servidor: En el archivo data.py, reemplaza la URL base de la plataforma Urban Routes con la URL del servidor proporcionada
3. Abrir PyCharm: Abre el proyecto en PyCharm:
4. Selecciona la carpeta del proyecto qa-project-Urban-Routes-es.
5. Ejecutar las pruebas: Una vez configurado el proyecto, puedes ejecutar las pruebas con Pytest. En la terminal de PyCharm, ejecuta el siguiente comando:
    pytest main.py
6. Resultados de las Pruebas: Las pruebas se ejecutarán en el navegador Google Chrome. Si todas las pruebas pasan correctamente, verás un resultado positivo en la terminal.


## Pasos de las Pruebas
Las pruebas automatizadas cubren los siguientes pasos del proceso de pedir un taxi:

1. **Configurar la dirección**: La dirección se configura automáticamente en las pruebas.
2. **Seleccionar la tarifa Comfort**: El proceso de selección de tarifa se verifica para asegurarse de que se pueda seleccionar la opción correcta.
3. **Rellenar el número de teléfono**: Se introduce un número de teléfono válido, y el código de confirmación se intercepta automáticamente.
4. **Agregar una tarjeta de crédito**: Se ingresa el número de tarjeta y el código CVV, y se espera a que el formulario se complete correctamente.
5. **Escribir un mensaje para el conductor**: Se simula la entrada de un mensaje en el campo correspondiente.
6. **Pedir una manta y pañuelos**: Se verifica que los elementos adicionales se puedan añadir correctamente.
7. **Pedir 2 helados**: Se verifica la adición de helados a la orden.
8. **Aparece el modal para buscar un taxi**: Se espera a que aparezca el modal con la información del conductor.



## Estructura del Proyecto
El proyecto está organizado de la siguiente manera:

qa-project-Urban-Routes-es/
│
├── main.py                # Aquí es donde se definen las pruebas automatizadas que cubren todo el flujo de la aplicación Urban Routes.
├── Metodos.py             # Contiene los métodos utilizados para interactuar con los elementos de la página web.
├── data.py                # Almacena la información sensible como números de tarjeta de crédito y configuraciones de la plataforma.
├── Codigo_phone.py        # Contiene la función retrieve_phone_code() que intercepta el código de confirmación para agregar una tarjeta de crédito.
├── requirements.txt       # Archivo que lista todas las dependencias de Python necesarias para ejecutar el proyecto.
└── README.md              # Este archivo

