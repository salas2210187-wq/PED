"""
Nombre: Gonzalez Salas Yuvia Itzel
Grupo: 951

"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def navegacion(Producto, paginas):
    s = Service(ChromeDriverManager().install()) #En caso de no tener el webdriver, lo instala
    opc = Options()
    opc.add_argument("--window-size=1200x1800")
    navegador = webdriver.Chrome(service=s,options=opc)
    navegador.get("https://www.amazon.com.mx/") #ir a una pagina definida
    time.sleep(2) #pausa y luego la siguiente linea de codigo

    #En caso de que aparezca la ventana para continuar a compras
    try:
        continuarCompras = WebDriverWait(navegador, 3).until(EC.element_to_be_clickable(By.CLASS_NAME, "a-button-text"))
        continuarCompras.click()
        time.sleep(1)
    except:
        print("La ventana no apareció, podemos continuar.")

    #Busqueda
    txtSearch = navegador.find_element(By.ID, "twotabsearchtextbox")
    txtSearch.send_keys(Producto)
    #Dar click en buscar
    buscar = navegador.find_element(By.ID, "nav-search-submit-button")
    buscar.click()
    time.sleep(2)

    for pag in range(0,paginas):
        navegador.execute_script("window.scrollTo(0, 450);") #Baja un poco y poder ver los productos
        time.sleep(1.5)

        #Validar si boton 'Siguiente' esta disponiblez
        try:
            navegador.save_screenshot(f"imagenes/Captura de Amazon #{pag+1}.png")
            next = WebDriverWait(navegador,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-button-accessibility.s-pagination-separator")))
            next.click()
        except:
            print("El botón 'Siguiente' ya no está disponible")
            break

    navegador.close()

if __name__ == '__main__':
    Producto = "Audífonos"
    paginas = 1
    navegacion(Producto, paginas)
