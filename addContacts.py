from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from sys import argv
from os import environ
import pandas as pandas



#Alertas plataforma info
url = "";
alertasUser = environ['alertasUser'];
alertasPassword = environ['alertasPassword'];
#Alertas plataforma info

#Lote info
nombreDeLote = "";
nombreDeColumnaConNombres = "";
nombreDeColumnaConTelefonos = "";
#Lote info

#Manejo de argumentos
if argv[1]:
    nombreDeLote = argv[1];

if argv[2]:
    nombreDeColumnaConNombres = argv[2];

if argv[3]:
    nombreDeColumnaConTelefonos = argv[3];

if argv[4]:
    if argv[4] == 'uywenance':
        url = 'http://uywenance.sondeosglobal.com/user/login';
    elif argv[4] == 'arwenance':
        url = 'http://arwenance.sondeosglobal.com/user/login';
#Manejo de argumentos


#Pandas
loteExcel = pandas.read_excel(nombreDeLote);
columnaNombresDelLote = loteExcel[nombreDeColumnaConNombres];
columnaNTelefonosDelLote = loteExcel[nombreDeColumnaConTelefonos];
#Pandas

#Selenium
browser = webdriver.Firefox();
browser.get(url);
#Selenium

#INICIO LOGUEO
usernameInput = browser.find_element_by_xpath("//input[@name='_username']");
passwordInput = browser.find_element_by_xpath("//input[@name='_password']");

#Consigue credenciales mediante variables de ambiente
usernameInput.send_keys(alertasUser);
passwordInput.send_keys(alertasPassword);
#Consigue credenciales mediante variables de ambiente

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