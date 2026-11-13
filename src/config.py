import logging
from datetime import datetime
from pathlib import Path

# Carpeta raíz del proyecto.
BASE_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "airbnb.db"
EXPORTS_DIR = DATA_DIR / "exports"
#BI_DIR = DATA_DIR / "bi"

# Respaldo de archivos CSV descargados sino se usa mongo.
ARCHIVOS_CSV = {
    "Listings": "listings",
    "Reviews": "reviews",
    "Calendar": "calendar",
}

# Conexión a MongoDB.
MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "airbnb_mx"


#Configuración de logs.
def configurar_logs() -> None:
    logger = logging.getLogger()
    if logger.handlers:
        return

    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    fecha_hora = datetime.now().strftime("%Y%m%d_%H%M")
    archivo_log = LOGS_DIR / f"etl_{fecha_hora}.txt"

    formato = logging.Formatter(
        "%(asctime)s - %(levelname)s - [%(module)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    archivo = logging.FileHandler(archivo_log, encoding="utf-8")
    archivo.setFormatter(formato)

    consola = logging.StreamHandler()
    consola.setFormatter(formato)

    logger.setLevel(logging.INFO)
    logger.addHandler(archivo)
    logger.addHandler(consola)
