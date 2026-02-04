import requests
import sys


def api(page):
    url = f"https://rickandmortyapi.com/api/character?page={page}"

    payload = ""
    headers = {}

    return requests.get( url)

def main():
    page = 1
    while True:
        dados = api(page)
        data = dados.json()
        if dados.status_code == 200:
            total_page = data["info"]["pages"]
            for result in data["results"]:
                nome = result["name"]
                status = result["status"]
                if status == "Alive":
                    print("-" * 60)
                    print(nome,status)

            if page < total_page:
                page+=1
            else:
                sys.exit()
        else:
            sys.exit()

if __name__ == "__main__":
    main()
