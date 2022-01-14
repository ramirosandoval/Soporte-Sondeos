from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pandas


#Pandas
loteExcel = pandas.read_excel('BASE UY 5.xlsx');
columnaNombresDelLote = loteExcel['Nombre'];
columnaNTelefonosDelLote = loteExcel['Tel WA'];
#Pandas

#Selenium
browser = webdriver.Firefox()
browser.get('http://uywenance.sondeosglobal.com')
#Selenium

#INICIO LOGUEO
usernameInput = browser.find_element_by_xpath("//input[@name='_username']")
passwordInput = browser.find_element_by_xpath("//input[@name='_password']")

usernameInput.send_keys("admin")
passwordInput.send_keys("admin.123")
browser.find_element_by_xpath("//button[@type='submit']").click()
#FIN LOGUEO

#Apretar boton de gestion de contactos
browser.find_element_by_xpath("//h4[text()='Gestion de Contactos']").click()

#Apretar boton de añadir
browser.find_element_by_xpath("//a[@class='btn btn-primary btn-sm glyphicon glyphicon-plus cursor-pointer']").click()

nombreDeContacto = browser.find_element_by_xpath("//input[@name='nombre']");
telefonoContacto = browser.find_element_by_xpath("//input[@name='telefono']");

counterLimit = 500;
counter = 0;
repetidosCounter = 0;

for nombre in columnaNombresDelLote:
    nombreDeContacto.send_keys(f"{nombre}")

    while counter<counterLimit:
        telefonoContacto.send_keys(f"{columnaNTelefonosDelLote[counter]}")
        counter+=1;
        break;

    try:
        browser.find_element_by_xpath("//input[@value='Guardar']").click();
        browser.find_element_by_xpath("//a[@class='btn btn-primary btn-sm glyphicon glyphicon-plus cursor-pointer']").click()
    except NoSuchElementException:
        repetidosCounter+=1;
        nombreDeContacto = browser.find_element_by_xpath("//input[@name='nombre']");
        telefonoContacto = browser.find_element_by_xpath("//input[@name='telefono']");

        nombreDeContacto.clear()
        telefonoContacto.clear()

        continue;

    nombreDeContacto = browser.find_element_by_xpath("//input[@name='nombre']");
    telefonoContacto = browser.find_element_by_xpath("//input[@name='telefono']");


print(f"El lote tuvo {repetidosCounter} numeros repetidos!");