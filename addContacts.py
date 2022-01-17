from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from os import environ
import argparse
import pandas as pandas

#Alertas plataforma info
url = None;

if environ.get('alertasUser'):
    alertasUser = environ['alertasUser'];

if environ.get('alertasPassword'):
    alertasPassword = environ['alertasPassword'];

#Alertas plataforma info

#Lote info
nombreDeLote = None;
nombreDeColumnaConNombres = None;
nombreDeColumnaConTelefonos = None;
#Lote info

#Manejo de argumentos

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--username', help='Username de la plataforma');
parser.add_argument('-p', '--password', help='Password de la plataforma');
parser.add_argument('-n', '--nombrelote', help='Nombre del lote');
parser.add_argument('-cn', '--columnanombres', help='Nombre de la columna con los nombres dentro del lote');
parser.add_argument('-ct', '--columnatelefonos', help='Nombre de la columna con los telefonos dentro del lote');
parser.add_argument('-l', '--link', help='Link o nombre de la plataforma en la que ingresar los contactos. Por EJ: eswenance (o la URL completa)');

args = parser.parse_args();


if args.nombrelote:
    nombreDeLote = args.nombrelote;

if args.columnanombres:
    nombreDeColumnaConNombres = args.columnanombres;

if args.columnatelefonos:
    nombreDeColumnaConTelefonos = args.columnatelefonos;

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
#Manejo de argumentos


#Pandas
loteExcel = pandas.read_excel(f"./bases/{nombreDeLote}");
columnaNombresDelLote = loteExcel[nombreDeColumnaConNombres];
columnaNTelefonosDelLote = loteExcel[nombreDeColumnaConTelefonos];
#Pandas

print(columnaNombresDelLote[0]);
print(columnaNTelefonosDelLote[0]);


#Selenium
browser = webdriver.Firefox();
browser.get(url);
#Selenium

#INICIO LOGUEO
usernameInput = browser.find_element_by_xpath("//input[@name='_username']");
passwordInput = browser.find_element_by_xpath("//input[@name='_password']");

#Consigue credenciales mediante variables de ambiente o argumentos
if argv.username and argv.password:
    usernameInput.send_keys(argv.username);
    passwordInput.send_keys(argv.password);
else:
    usernameInput.send_keys(alertasUser);
    passwordInput.send_keys(alertasPassword);
#Consigue credenciales mediante variables de ambiente o argumentos

#Clickea boton de logueo
browser.find_element_by_xpath("//button[@type='submit']").click();
#FIN LOGUEO

#Apretar boton de gestion de contactos
browser.find_element_by_xpath("//h4[text()='Gestion de Contactos']").click();

#Apretar boton de añadir
browser.find_element_by_xpath("//a[@class='btn btn-primary btn-sm glyphicon glyphicon-plus cursor-pointer']").click();

elementoNombreDeContacto = browser.find_element_by_xpath("//input[@name='nombre']");
elementoTelefonoContacto = browser.find_element_by_xpath("//input[@name='telefono']");

counterLimit = 500;
counter = 0;
repetidosCounter = 0;
counterForConsoleLog = 0;

print(f"Lote seleccionado: {nombreDeLote}");

for nombre in columnaNombresDelLote: #Por cada nombre en el lote
    elementoNombreDeContacto.send_keys(f"{nombre}");#ingresa el nombre tomado en la iteracion actual

    while counter<counterLimit:#Y, mientras no se hayan cargado todos los contactos,
        elementoTelefonoContacto.send_keys(f"{columnaNTelefonosDelLote[counter]}");#ingresar el telefono correspondiente al nombre tomado
        counter+=1;#aumentar contador de informacion de contactos cargada.
        break; # salir de la iteracion del while

    try:#Intenta:
        browser.find_element_by_xpath("//input[@value='Guardar']").click();#clickear el boton de guardar una vez ingresada la info, si es exitoso redirige a la pagina anterior.
        browser.find_element_by_xpath("//a[@class='btn btn-primary btn-sm glyphicon glyphicon-plus cursor-pointer']").click();#Volver a la pagina de suma de contacto
        counterForConsoleLog+=1;#aumentar contador de numeros cargados exitosamente
        print(f"Se han cargado {counterForConsoleLog} numeros exitosamente!");#Mostrar en consola los contactos cargados exitosamente (valor del contador anterior).
    except NoSuchElementException:#Si al apretar el boton de guardar se detecta que el usuario ya existia, jamas redirige a la pagina anterior, por lo que no
    #se encuentra el boton de añadir nuevo contacto, devolviendo asi una exepcion "NoSuchElement". Si esto sucede:
        repetidosCounter+=1;#aumentar contador de contactos repetidos
        elementoNombreDeContacto = browser.find_element_by_xpath("//input[@name='nombre']");#Volver a encontrar el input de nombre
        elementoTelefonoContacto = browser.find_element_by_xpath("//input[@name='telefono']");#Volver a encontrar el input de telefono

        elementoNombreDeContacto.clear();#Borrar el nombre del contacto repetido
        elementoTelefonoContacto.clear();#Borrar el telefono del contacto repetido

        continue; #Y pasar al siguiente contacto.

    elementoNombreDeContacto = browser.find_element_by_xpath("//input[@name='nombre']");#Volver a encontrar el input de nombre
    elementoTelefonoContacto = browser.find_element_by_xpath("//input[@name='telefono']");#Volver a encontrar el input de telefono


print(f"El lote tuvo {repetidosCounter} numeros repetidos!");