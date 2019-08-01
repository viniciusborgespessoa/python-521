import requests

URL = 'https://gen-net.herokuapp.com/api/users/{}'

user_id = input('Digite seu ID: ')
email = input('Digite o seu email: ')
name = input('Digite seu nome: ')
password = input('Digite sua senha: ')


payload = {
	'name': name,
	'email': email,
	'password': password
}

r = requests.put(URL.format(user_id), payload)

if r.status_code == 200:
	print("Usuário atualizado com sucesso")
else:
	print("Erro ao atualizar o usuário")

