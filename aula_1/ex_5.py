import requests

URL = 'https://gen-net.herokuapp.com/api/users/'
response = requests.get(URL)
resultado = response.json()

email = input('Digite o E-Mail do Usuário: ')

for user in resultado:
	if user.get('email') == email:
		print(user)

