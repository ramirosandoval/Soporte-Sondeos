from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pandas
from sys import argv
import argparse

#Inicializacion de variables necesarias
url = None;
nombreDeLote = None;
nombreDeColumnaConNombres = None;
nombreDeGrupo = None;
codigoDeGrupo = None;
nombreDeColumnaConMensajes = None;
#Inicializacion de variables necesarias


#Argumentos

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--username', help='Username de la plataforma');
parser.add_argument('-p', '--password', help='Password de la plataforma');
parser.add_argument('-nl', '--nombrelote', help='Nombre del lote');
parser.add_argument('-ng', '--nombregrupo', help='Nombre del grupo');
parser.add_argument('-cg', '--codigogrupo', help='Codigo del grupo');
parser.add_argument('-cn', '--columnanombres', help='Nombre de la columna con los nombres dentro del lote');
parser.add_argument('-cm', '--columnamensajes', help='Nombre de la columna con los mensajes dentro del lote');
parser.add_argument('-l', '--link', help='Link o nombre de la plataforma en la que ingresar los contactos. Por EJ: eswenance (o la URL completa)');

args = parser.parse_args();


if args.nombrelote:
    nombreDeLote = args.nombrelote;

if args.columnanombres:
    nombreDeColumnaConNombres = args.columnanombres;

if args.columnamensajes:
    nombreDeColumnaConMensajes = args.columnamensajes;

if args.link:
    if args.link == 'uywenance':
        url = 'http://uywenance.sondeosglobal.com/user/login';
    elif args.link == 'arwenance':
        url = 'http://arwenance.sondeosglobal.com/user/login';
    elif args.link == 'argenpesos':
        url = 'http://argenpesos.sondeosglobal.com/user/login';
    elif args.link == 'eswenance':
        url='http://eswenance.sondeosglobal.com/user/login';
    else:
        url = args.link;

if args.nombregrupo:
    nombreDeGrupo = args.nombregrupo;
     
if args.codigogrupo:
    codigoDeGrupo = args.codigogrupo;
#Argumentos

#Pandas
loteExcel = pandas.read_excel(f"./bases/{nombreDeLote}");
columnaNombresDelLote = loteExcel[nombreDeColumnaConNombres];
columnaMensajesDelLote = loteExcel[nombreDeColumnaConMensajes]
#Pandas

#Selenium init
browser = webdriver.Firefox();
browser.get(url);
#Selenium init

#Login
usernameInput = browser.find_element_by_xpath("//input[@name='_username']");
passwordInput = browser.find_element_by_xpath("//input[@name='_password']");

#Credentials
if args.username and args.password:
    usernameInput.send_keys(args.username);
    passwordInput.send_keys(args.password);
#Credentials


browser.find_element_by_xpath("//button[@type='submit']").click();
#Login

#Creating new group BEGINNING
browser.find_element_by_xpath("//h4[text()='Gestion de Grupos']").click();

browser.find_element_by_xpath("//a[@class='btn btn-primary btn-sm glyphicon glyphicon-plus cursor-pointer']").click();

elementoNombreDeGrupo = browser.find_element_by_xpath("//input[@name='nombre']");
elementoCodigoDeGrupo = browser.find_element_by_xpath("//input[@name='codigo']");
inputContactos = browser.find_element_by_xpath("//input[@placeholder='Selecciones contactos']");

elementoNombreDeGrupo.send_keys(nombreDeGrupo);
elementoCodigoDeGrupo.send_keys(codigoDeGrupo);
counterForConsoleLog = 0;
counterForErrorConsoleLog = 0;

print(f"Lote seleccionado: {nombreDeLote}");

#Por cada nombre en el lote
for nombre in columnaNombresDelLote:

    #Intenta llenar la informacion pedida en la pagina con la informacion referente al nombre sobre el que se este iterando
    try:
        inputContactos.send_keys(f"{nombre}");
        #TODO: encapsular esto en una funcion con un nombre descriptivo "escribirNombreDelContactoYSeleccionarlo()".
        browser.find_element_by_xpath("//li[@class='select2-results__option select2-results__option--highlighted']").click();

        #TODO: encapsular esto en una funcion con un nombre descriptivo "mostrarEnConsolaElLogDeContactoAñadidoAlInput()".
        counterForConsoleLog+=1;
        print(f"Cantidad de contactos añadidos al input: {counterForConsoleLog}!");
    
    #Si el usuario, por cualquier motivo no es encontrado por la pagina
    except NoSuchElementException:
        #Borrar el nombre del mismo
        browser.find_element_by_xpath("//input[@class='select2-search__field']").clear();

        #TODO: encapsular esto en una funcion con un nombre descriptivo "mostrarEnConsolaElLogDeContactoNoEncontrado()".
        counterForErrorConsoleLog+=1;
        print(f"Cantidad de contactos que no se encontraron: {counterForErrorConsoleLog}!");

        #Y pasar al siguiente nombre
        continue;


#Ingresar mensaje al grupo
browser.find_element_by_xpath("//input[@name='mensaje']").send_keys(columnaMensajesDelLote[0]);

#Finalmente, guardar grupo con todos los contactos.
browser.find_element_by_xpath("//input[@value='Guardar']").click();