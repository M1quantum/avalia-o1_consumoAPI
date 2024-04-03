import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            print("CEP:", data['cep'])
            print("Logradouro:", data['logradouro'])
            print("Complemento:", data.get('complemento', ''))
            print("Bairro:", data['bairro'])
            print("Cidade:", data['localidade'])
            print("Estado:", data['uf'])
        else:
            print("CEP não encontrado.")
    else:
        print("Falha ao consultar o CEP.")

if __name__ == "__main__":
    cep = input("Digite o CEP para consulta: ")
    consultar_cep(cep)