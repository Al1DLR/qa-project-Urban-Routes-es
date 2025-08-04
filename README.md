Proyecto Sprint #8 – QA Project Urban Routes-es
Autor: Alisson De La Rosa
Cohorte: 30

Este proyecto automatiza pruebas para la aplicación Urban Routes, 
simulando el flujo de un usuario que solicita un taxi con 
características específicas y completando los datos requeridos por 
la aplicación.

Requisitos
Python 3.10+
PyCharm u otro editor compatible
Librerías necesarias:
pip install selenium pytest.

Estructura del proyecto
data.py → Contiene los datos que se usarán para rellenar los campos requeridos.

locators.py → Contiene los localizadores de los elementos que se deben encontrar o hacer clic.

methods.py → Incluye las funciones que ejecutan las acciones necesarias para la prueba.

main_test.py → Contiene los casos de prueba y los ejecuta.

Ejecución de pruebas
Para ejecutar los casos de prueba: pytest main_test.py

Descripción del flujo de prueba
El script abre la aplicación Urban Routes en el navegador.

Ingresa los datos del viaje (origen y destino).

Selecciona características específicas del taxi.

Completa los datos personales solicitados por la aplicación.

Verifica que la solicitud se realice correctamente.