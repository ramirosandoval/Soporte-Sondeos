from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pandas
from sys import argv
from os import environ

alertasUser = environ['alertasUser'];
alertasPassword = environ['alertasPassword'];

#Inicializacion de variables necesarias
url = "";
nombreDeLote = "";
nombreDeColumnaConNombres = "";
nombreDeGrupo = "";
codigoDeGrupo = 0;
nombreDeColumnaConMensajes = "";
#Inicializacion de variables necesarias


#Asignacion de argumentos como valor de variables
if argv[1]:
    nombreDeLote = argv[1];

if argv[2]:
    nombreDeColumnaConNombres = argv[2];

if argv[3]:
    nombreDeColumnaConMensajes = argv[3];

if argv[4]:
    if argv[4] == 'uywenance':
        url = 'http://uywenance.sondeosglobal.com/user/login';
    elif argv[4] == 'arwenance':
        url = 'http://arwenance.sondeosglobal.com/user/login';
    elif argv[4] == 'argenpesos':
        url = 'http://argenpesos.sondeosglobal.com/user/login';
    else:
        url = argv[4];

if argv[5]:
    nombreDeGrupo = argv[5];
     
if argv[6]:
    codigoDeGrupo = argv[6];
#Asignacion de argumentos como valor de variables


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
usernameInput.send_keys(alertasUser);
passwordInput.send_keys(alertasPassword);
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