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
import pandas as pd
from bs4 import BeautifulSoup


def extraer(html,d):
    soup = BeautifulSoup(html, "html.parser")
    productos = soup.find_all("div", class_="a-section a-spacing-small puis-padding-left-small puis-padding-right-small")
    for producto in productos:
        #Extraer el nombre del producto
        nombre = producto.find("a", class_="a-link-normal s-line-clamp-4 s-link-style a-text-normal")
        if nombre:
            d["Nombre"].append(nombre.text)
        else:
            d["Nombre"].append("Nombre no disponible")

        #Extraer el precio del producto
        precioEntero = producto.find("span", class_="a-price-whole")
        precioCentavo = producto.find("span", class_="a-price-fraction")
        if precioEntero and precioCentavo:
            precio = f"{precioEntero.get_text()}{precioCentavo.get_text()}"
            d["Precio"].append(precio)
        else:
            d["Precio"].append("Precio no disponible")

        #Extraer la fecha de entrega del producto
        fecha = producto.find("span", class_="a-text-bold")
        if fecha:
            d["Fecha de entrega"].append(fecha.text)
        else:
            d["Fecha de entrega"].append("Fecha de entrega no disponible")

        #Extraer el rating
        rating = producto.find("span", class_="a-icon-alt")
        if rating:
            d["Rating"].append(rating.text)
        else:
            d["Rating"].append("Rating no disponible")
    print(d)

def navegacion(producto, paginas):
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1020x1200")
    navegador = webdriver.Chrome(service=s,options=opc)
    navegador.get("https://www.amazon.com.mx/")
    time.sleep(1)

    #En caso de que aparezca el boton "Continuar a compras"
    try:
        continuarCompras = WebDriverWait(navegador,3).until(EC.element_to_be_clickable(By.CLASS_NAME, "a.s-pagination-next"))
        continuarCompras.click()
    except:
        print("La ventana no apareció, podemos continuar.")

    #Buscar el producto
    txtSearch = navegador.find_element(By.ID, "twotabsearchtextbox")
    txtSearch.send_keys(producto)
    #Dar click en buscar
    buscar = navegador.find_element(By.ID, "nav-search-submit-button")
    buscar.click()
    time.sleep(1)

    #Guardar la info
    d = {"Nombre": [], "Precio": [], "Fecha de entrega": [], "Rating": []}

    for pag in range(0,paginas):
        time.sleep(2)
        extraer(navegador.page_source, d)
        try:
            next = WebDriverWait(navegador, 3).until(EC.element_to_be_clickable(By.CLASS_NAME, "a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-button-accessibility.s-pagination-separator"))
            next.click()
        except:
            print("El botón 'Siguiente' ya no está disponible")
            break

    navegador.close()

    df = pd.DataFrame(d)
    df.to_csv(f"datasets/Amazon.csv")
    return df

if __name__ == '__main__':
    producto = "Audífonos"
    paginas = 4
    navegacion(producto,paginas)