# Carga de lotes a plataformas de Alertas

## Dependencias:
<ul>
  <li>Pandas</li>
  <li>Selenium</li>
</ul>

## Instalacion:
<ul>
  Si no tienen instalado PIP, instalarlo con la ejecución del fichero que se obtiene aquí: https://bootstrap.pypa.io/get-pip.py. <pre><code class="shell">cd ~/Downloads && sudo python3 get-pip.py</code></pre>


  <li>Instalar las dependencias del script: <pre><code class="shell">sudo pip install selenium && sudo pip install pandas</code></pre></li>
  <li>Instalar webdriver de Selenium para Firefox (necesario para que selenium controle el browser), descargándolo desde https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz. (Extraerlo y dejar el archivo en /usr/local/bin con el comando <pre><code class="shell">sudo mv ~/Downloads/geckodriver /usr/local/bin/</code></pre></li>
  <li>Conseguir los scripts desde https://github.com/ramirosandoval/Soporte-Sondeos <pre><code class="shell">git clone https://github.com/ramirosandoval/Soporte-Sondeos</code></pre></li>
  <li>Ambos scripts se usan con el comando python3 _nombredescript.py_. Por Ejemplo: <pre><code class="shell">python3 addContacts.py --help</code></pre></li>
</ul>


## Flags de cada script

<p>El script addContacts toma 6 argumentos:</p>
<ul>
  <li>-u / —username es para indicar el nombre de usuario de la plataforma de alertas</li>
  <li>-p / —password es para indicar la contraseña de la plataforma de alertas</li>
  <li>-nl / —nombrelote es para indicar el nombre del lote seguido de su extension que tiene que estar en una carpeta llamada "bases", por ahora el programa solo trabaja con archivos excel.</li>
  <li>-cn / —columnanombres es para indicar el valor que tiene la columna que posee los nombres de contacto dentro del lote y que el programa la identifique.</li>
  <li>-ct / —columnatelefonos es para indicar el valor que tiene la columna que posee los telefonos de cada contacto dentro del lote.</li>
<li>-l / —link es para indicar el link o nombre de la plataforma en la que ingresar los contactos. Por EJ: eswenance/argenpesos/http://uywenance.sondeosglobal.com/user/login</li>
</ul>

<p>El script addGroup toma 8 argumentos, siendo 5 iguales al otro script:</p>
<ul>
  <li>-u / —username es para indicar el nombre de usuario de la plataforma de alertas</li>
  <li>-p / —password es para indicar la contraseña de la plataforma de alertas</li>
  <li>-nl / —nombrelote es para indicar el nombre del lote seguido de su extension que tiene que estar en una carpeta llamada "bases", por ahora el programa solo trabaja con archivos excel.</li>
  <li>-cn / —columnanombres es para indicar el valor que tiene la columna que posee los nombres de contacto dentro del lote y que el programa la identifique.</li>
  <li>-l / —link es para indicar el link o nombre de la plataforma en la que ingresar los contactos. Por EJ: eswenance/argenpesos/</li>
  <li>-ng / —nombregrupo es para indicar el nombre que se desea que tenga el grupo</li>
  <li>-cg / —codigogrupo es para indicar el codigo numerico que se desea que tenga el grupo</li>
  <li>-cm / —columnamensaje es para indicar el valor que tiene la columna que posee el mensaje que se enviara a cada contacto.</li>
</ul>

### A tener en cuenta

El programa, al ser ejecutado con todos sus parámetros especificados, tardara unos segundos en abrir el navegador y automáticamente ingresar los contactos o crear el grupo. Para su correcto funcionamiento es importante minimizar este navegador.
Los programas envian informacion sobre su estado hacia la consola.
