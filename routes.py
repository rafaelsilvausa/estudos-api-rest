import requests

pagina = 4

url = f"https://rickandmortyapi.com/api/character?page={pagina}"

payload = {}
headers = {}

response = requests.request("GET", url)
resposta = response.json()

if response.status_code == 200:
    paginas_total = resposta["info"]["pages"]
    for data in resposta["results"]:
        status = data["status"]
        nomes = data["name"]
        sp = data["species"]
        og = data["origin"]["name"]
        loc = data["location"]["url"]

        print(status)
        print(nomes)
        print(sp)
        print(og)
        print(loc)
        print('-' * 20)

