Análisis de Vehículos Usados

Una aplicación interactiva para explorar datos de automóviles usados en EE.UU.

🧭 Descripción

Este proyecto permite al usuario visualizar y analizar un conjunto de datos con anuncios de vehículos usados (en EE.UU.). Usando herramientas como Streamlit, Plotly Express y pandas, la aplicación ofrece:

Histogramas para observar la distribución del kilometraje (odómetro).

Diagramas de dispersión para ver la relación entre el año de modelo y el precio, diferenciando por tipo de vehículo.

Elementos interactivos (botones, checkboxes) para que el usuario seleccione qué visualización desea ver.

🚀 Cómo ejecutar la aplicación localmente

Clonar el repositorio:

git clone https://github.com/FallenAngel117/Analisis_de_Vehiculos_Usados.git  
cd Analisis_de_Vehiculos_Usados  


Crear un entorno virtual (recomendado) e instalar las dependencias:

python -m venv venv  
source venv/bin/activate   # en Linux/macOS  
venv\Scripts\activate      # en Windows  
pip install -r requirements.txt  


Ejecutar la aplicación:

streamlit run APP.py  


Luego abre el navegador en la dirección que indica Streamlit (p. ej. http://localhost:8501
).

📁 Estructura del repositorio

APP.py — Archivo principal que lanza la aplicación web.

vehicles_us.csv — Conjunto de datos con anuncios de vehículos usados.

notebooks/ — Carpeta que puede contener exploraciones, análisis de datos adicionales o notebooks de Jupyter.

requirements.txt — Listado de las librerías necesarias para la aplicación.

.gitignore — Archivos o carpetas que no se versionan.

🧠 Datos

El dataset vehicles_us.csv contiene información de anuncios de autos usados (EE.UU.). Incluye variables como: año del modelo, kilometraje, precio, tipo de vehículo, etc.
(Si lo deseas, puedes añadir aquí un enlace a la fuente del dataset o una breve descripción del origen de los datos.)

✅ ¿Por qué es útil?

Permite observar tendencias: por ejemplo, ¿cómo afecta el año del modelo al precio de un vehículo usado?

Facilita detectar patrones y outliers en el mercado de autos usados.

Es interactiva, lo que permite explorar los datos sin necesidad de escribir código adicional.

Buen punto de partida para proyectos más avanzados de análisis de datos, machine learning o visualización.

🛠 Mejoras o ideas futuras

Incluir filtros adicionales (marcas, modelos, ubicación geográfica).

Añadir predicción de precios usando modelos de machine learning.

Integrar más visualizaciones (mapas, gráficas de series temporales, etc.).

Desplegar la aplicación online para que sea accesible sin instalación.

📄 Licencia

Indicar la licencia que quieras usar (por ejemplo, MIT, GPL, etc.).
Por defecto, agrega:

MIT License — ver el archivo LICENSE para más información.

🙋 Contacto

Si tienes preguntas, sugerencias o deseas colaborar, puedes contactarme en GitHub o por email bryanfraustos@gmail.com.
   
