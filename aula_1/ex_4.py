import requests

URL = 'https://gen-net.herokuapp.com/api/users/{}'

id_usuario = input('Digite o ID do Usuário: ')

response = requests.get(URL.format(id_usuario))

print(response.json())