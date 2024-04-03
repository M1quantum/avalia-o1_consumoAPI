import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados_cep = resposta.json()
        if 'erro' not in dados_cep:
            print("CEP:", dados_cep['cep'])
            print("Logradouro:", dados_cep['logradouro'])
            print("Complemento:", dados_cep.get('complemento', ''))
            print("Bairro:", dados_cep['bairro'])
            print("Cidade:", dados_cep['localidade'])
            print("Estado:", dados_cep['uf'])
        else:
            print("CEP não encontrado.")
    else:
        print("Falha ao consultar o CEP.")

if __name__ == "__main__":
    cep = input("Digite o CEP para consulta: ")
    consultar_cep(cep)
