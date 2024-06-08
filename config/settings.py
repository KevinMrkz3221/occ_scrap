import os
import argparse
from datetime import date
from selenium import webdriver
from time import sleep
import pathlib

from controllers.writer import VacancyWriter
from controllers.scrapper import Scrapper


def SLEEP():
    sleep(args.sleep)

# Argumentos que se le pueden agregar al utilizar python main.py 
parser = argparse.ArgumentParser(description="OCC Scrapper")
parser.add_argument('--url', '-u', help="Agrega el url donde quieres iniciar el scraping Ejemplo: -u https://url.com")
parser.add_argument('--sleep', '-s', type=int, help="Agrega el tiempo de sleep en segundos Ejemplo: -s 3")
parser.add_argument('--name', '-n', type=str, help='Agrega el nombre del archivo Ejemplo: -n Chihuahua_today')
## 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--start-maximized")


# Parsea los argumentos de la línea de comandos
args = parser.parse_args()

#
MAIN_URL = 'https://www.occ.com.mx/'


try:
    os.mkdir('C:\\OCC_DATA')
except Exception as E:
    print(f"La ruta de descarga ya existe \n {E}")

# Json Name
JSON_FILE = f"C:\\OCC_DATA\\{args.name}_{date.today()}.json"

if not pathlib.Path(JSON_FILE).exists():
    
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        f.write("[]")
        f.close()

vacancyController = VacancyWriter(JSON_FILE)
SCRAPER = Scrapper(args, vacancyController, chrome_options, SLEEP)

## 

