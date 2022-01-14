from selenium import webdriver
from selenium import webdriver
import pandas as pandas

loteExcel = pandas.read_excel('BASE 1 ARGENTINA.xlsx');
columnaNombresDelLote = loteExcel['NOMBRE Y APELLIDO'];

browser = webdriver.Firefox()
browser.get('http://arwenance.sondeosglobal.com')

usernameInput = browser.find_element_by_xpath("//input[@name='_username']")
passwordInput = browser.find_element_by_xpath("//input[@name='_password']")

usernameInput.send_keys("admin")
passwordInput.send_keys("admin.123")

browser.find_element_by_xpath("//button[@type='submit']").click()
browser.find_element_by_xpath("//h4[text()='Gestion de Grupos']").click()

browser.find_element_by_xpath("//a[@class='btn btn-primary btn-sm glyphicon glyphicon-plus cursor-pointer']").click()

nombreDeGrupo = browser.find_element_by_xpath("//input[@name='nombre']")
codigoDeGrupo = browser.find_element_by_xpath("//input[@name='codigo']")
inputContactos = browser.find_element_by_xpath("//input[@placeholder='Selecciones contactos']")

nombreDeGrupo.send_keys("Test grupo random");
codigoDeGrupo.send_keys("69420");

for nombre in columnaNombresDelLote:

    print(inputContactos.send_keys(f"{nombre}"));
    browser.find_element_by_xpath("//li[@class='select2-results__option select2-results__option--highlighted']").click();
