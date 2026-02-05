import requests
from dotenv import load_dotenv
import sys
import os

load_dotenv()
key = os.getenv("KEY")
id = os.getenv("ID")
def api (page):
    url = f"https://api.alephcrm.com/v2/products?accountId={id}&api_key={key}"

    payload = {}
    headers = {
    'Accept': 'application/json'
    }

    return requests.get(url, headers=headers, data=payload)

def main():
    pages = 0
    while True:
        dado = api(pages)
        data = dado.json()
        if dado.status_code == 200:
            total_pages = data["Paging"]["Offset"]
            for res in data["Results"]:
                sku = res["Identification"]["SKU"]
                if sku == "AC 25001" :
                    print("-"*80)
                    for i in res["Price"]:
                        preco = i["Price"]
                        print(f" o preço de {sku} é {preco}")
                    qd = res["Stock"]["Quantity"]
                    print(f"Sua quantidade em estoque é: {qd}")
                    print("-"*80)
        if pages < total_pages:
            pages+=100
        else:
            sys.exit()      
                



if __name__ == "__main__":
    main()
