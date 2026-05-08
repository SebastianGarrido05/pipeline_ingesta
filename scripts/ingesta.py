import shutil, os, logging
from datetime import datetime

# 1. Configurar logging (escribe en archivo Y en consola)
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/ingesta.log'),
        logging.StreamHandler()
    ]
)

# 2. Funcion de ingesta (reutilizable y testeable)
def ingestar(origen, destino_carpeta):
    os.makedirs(destino_carpeta, exist_ok=True)
    nombre = os.path.basename(origen)
    destino = os.path.join(destino_carpeta, nombre)
    logging.info(f'Iniciando ingesta: {origen}')
    try:
        shutil.copy(origen, destino)
        logging.info(f'[OK] Copiado a: {destino}')
    except FileNotFoundError:
        logging.error(f'[ERROR] No encontrado: {origen}')
        raise

# 3. Ejecutar
if __name__ == '__main__':
    ingestar('datos_prueba.csv', 'data/raw')
    logging.info('Ingesta completada.')