import requests
import sys
def api(pages):
    url = f"https://rickandmortyapi.com/api/character?page={pages}"

    payload = ""
    headers = {}

    return requests.get(url)

def main():
    pages = 1
    data = api(pages)
    dados = data.json()
    if data.status_code == 200:
        pages_total = dados["info"]["pages"]
        for resultado in dados["results"]:
            nome = resultado["name"]
            status = resultado["status"]
            especie = resultado["species"]

            print('-' * 60)
            print(nome,status,especie)

            if pages < pages_total:
                pages+=1
            else:
                sys.exit()
    else:
        sys.exit()

if __name__ == "__main__":
    main()