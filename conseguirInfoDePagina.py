from selenium import webdriver;
from selenium.common.exceptions import NoSuchElementException;
import argparse, os;

#--- Definicion de argumentos del script START---#
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pagina', help='Link de la pagina de la que se desea obtener informacion')
args = parser.parse_args()
#--- Definicion de argumentos del script END---#

#--- Leer variable de entorno para saber que cuenta de capiwha utilizar START---#
variableDeEntornoCapiwha = os.getenv('proximoUsuarioDeCapiwhaDebeSerApiwha')
capiwhaFueVisitado = None

if variableDeEntornoCapiwha == 1:
    capiwhaFueVisitado = True
    print(f'Capiwha fue visitado anteriormente: valor de variable = {capiwhaFueVisitado}')
else:
    capiwhaFueVisitado = False
    print(f'Capiwha NO fue visitado anteriormente: valor de variable = {capiwhaFueVisitado}')

#--- Leer variable de entorno para saber que cuenta de capiwha utilizar END---#


if args.pagina == None:
    print('Es obligatorio indicar de que pagina se quiere obtener la informacion (parametro \"-p\" o \"--pagina\")')
else:

    firefoxDriver = webdriver.Firefox()

    if args.pagina == 'panel.capiwha.com' and capiwhaFueVisitado == False:
        capiwhaFueVisitado = True
        setearVariableDeEntornoCapiwha()

    firefoxDriver.get(f'http://{args.pagina}')

