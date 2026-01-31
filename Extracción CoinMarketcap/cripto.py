import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url_base = "https://coinmarketcap.com/?page={}"
Lista_monedas = []
headers = {'User-Agent': 'Mozilla/5.0'}

# Usamos rango hasta 35 para asegurar las 500 monedas
for i in range(1, 40):
    print(f"Procesando página {i}... (Criptos acumuladas: {len(Lista_monedas)})")
    response = requests.get(url_base.format(i), headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    cripto_moneda = soup.select('table.cmc-table tbody tr')

    for fila in cripto_moneda:
        try:
            # 1. Extracción de textos
            Nombre = fila.find('p', class_="coin-item-name").text.strip()
            Simbolo = fila.find('p', class_="coin-item-symbol").text.strip()

            # Sacamos los valores raw (con $, comas y letras)
            precio_raw = fila.select_one('td:nth-of-type(4)').text.strip()
            mcap_raw = fila.select_one('td:nth-of-type(8)').text.strip()
            vol_raw = fila.select_one('td:nth-of-type(9)').text.strip()

            # 2. TRATAMIENTO DE DATOS
            # Limpiamos el precio: quitamos $, comas y pasamos a float
            Precio = float(precio_raw.replace('$', '').replace(',', ''))

            # Limpiamos Market Cap y Volumen (Ojo: CMC a veces usa "B" o "M")
            # Para cumplir la tarea simplemente quitamos $ y comas
            Market_Cap = mcap_raw.replace('$', '').replace(',', '')
            Volumen_24h = vol_raw.replace('$', '').replace(',', '')

            Lista_monedas.append({
                'Nombre': Nombre,
                'Símbolo': Simbolo,
                'Precio': Precio,
                'Market_Cap': Market_Cap,
                'Volumen_24h': Volumen_24h
            })

            # Parar al llegar a 500
            if len(Lista_monedas) >= 500: break
        except:
            continue

    if len(Lista_monedas) >= 500: break
    time.sleep(2)

# 4. Guardamos en CSV
df = pd.DataFrame(Lista_monedas)
df.to_csv('cripto_data.csv', index=False, encoding='utf-8-sig')
print(f"¡Tarea completada! Se guardaron {len(Lista_monedas)} monedas tratadas.")