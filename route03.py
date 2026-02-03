import requests
import sys

def api(page):
    url = f"https://rickandmortyapi.com/api/character?page={page}"

    payload = {}
    headers = {}

    return requests.get(url)

def main ():
    page = 1

    while True:
        dados = api(page)
        if dados.status_code == 200:
            data_jason = dados.json()
            page_total = data_jason["info"]["pages"]
            for resultado in data_jason["results"]:
                nome = resultado["name"]
                especie = resultado["species"]
                print("-"*50)
                print(nome,especie)
                print(page)


                if page < page_total:
                    page+=1
                    
                else:
                    sys.exit()
                

if __name__ == "__main__":
    main()