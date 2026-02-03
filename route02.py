import requests
import sys


def api(page):
    url = f"https://rickandmortyapi.com/api/character?page={page}"

    payload = {}
    headers = {}

    return requests.get( url)


def main ():
    page = 1
    

    while True :
        dados = api(page)
        if dados.status_code == 200:
            tata_jason = dados.json()
            page_total = tata_jason['info']['pages']
            for resultado in tata_jason["results"]:
                nome = resultado["name"]
                status = resultado["status"]
                genero = resultado["gender"]
                specie = resultado["species"]
                orig = resultado["origin"]["name"]

                print(nome,genero,status,specie,orig)

            print(page)
            print('-' * 50)
            if page < page_total:
                
                page+=1
            else:
                sys.exit()
                print(page)
                
        else:
            print(dados.status_code)
            print(dados.text)
            sys.exit()
      















    # while True:
    #     dado = api(page)
    #     if dado.status_code == 200:
    #         data_json = dado.json()
    #         pagina_total = data_json['info']['pages']

    #         for info in data_json['results']:
    #             nome = info['name']
    #             print(nome)

    #         print('-' * 50)
    #         print(page)
    #         if page <= pagina_total:
    #             page += 1
    #         else:
    #             sys.exit()

if __name__ =='__main__':
    main()

# if __name__ == '__main__':
#     main()