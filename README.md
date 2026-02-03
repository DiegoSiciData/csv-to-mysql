#  CSV to MySQL Data Processor (Python)

##  Descripción
Este proyecto consiste en un script en Python desarrollado como simulación de encargo freelance, cuyo objetivo es procesar, limpiar y validar datos desde archivos CSV para luego insertarlos de forma segura en una base de datos MySQL.

El sistema contempla validaciones de datos, manejo de errores y registro de incidencias, replicando un escenario real de carga de información desde fuentes no confiables.

---

## Problema que resuelve
Muchos negocios reciben datos en archivos CSV con:
- Campos vacíos
- Emails mal formateados
- Tipos de datos incorrectos
- Errores humanos frecuentes

Este script automatiza la detección de errores, evita insertar información inválida y deja trazabilidad mediante logs.

---

## Tecnologías utilizadas
- Python 3
- MySQL
- mysql-connector-python
- CSV (librería estándar)
- Logging

---

## Estructura del proyecto
```
csv_to_mysql/
│
├── data/
│   └── clientes.csv
│
├── logs/
│   └── errores.log
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Funcionalidades principales
- Lectura de archivos CSV
- Limpieza de datos
- Validación de campos obligatorios
- Validación de formato de email
- Conversión segura de tipos de datos
- Inserción en base de datos MySQL
- Manejo de errores sin detener el proceso
- Registro de errores en archivo de log

---

## 🗄️ Estructura de la base de datos
```sql
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    edad INT
);
```
## Cómo ejecutar el proyecto
1 Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/csv_to_mysql.git
cd csv_to_mysql
```

2 Instalar dependencias
```bash
pip install -r requirements.txt
```
3 Configurar la base de datos

Editar el archivo config.py con tus credenciales MySQL.
4 Ejecutar el script
```bash
python main.py
```

## Registro de errores

Las filas inválidas se registran automáticamente en el archivo:

logs/errores.log


Ejemplo de error registrado:

Fila inválida {'nombre': 'Ana', 'email': 'ana@email.com', 'edad': 'abc'} | Edad inválida

## Caso de uso

Limpieza de datos

Migración de información

Automatización de cargas

Validación previa a análisis de datos

## Autor

Proyecto desarrollado por Diego Sade
Como simulación de encargo freelance para fines de portafolio profesional.

## Posibles mejoras futuras

Soporte para múltiples archivos CSV

Variables de entorno

Reporte final de procesamiento

Exposición del script como API REST