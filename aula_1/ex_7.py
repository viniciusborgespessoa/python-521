import requests

URL = 'https://gen-net.herokuapp.com/api/users/'
URL2 = 'https://gen-net.herokuapp.com/api/users/'


payload = {
	'name': input('Digite seu nome: '),
	'email': input('Digite o seu email: '),
	'password': input('Digite sua senha: ')
}


res = requests.post(URL, payload)

if res.status_code == 200:
	user_id = res.json().get('id')
	print("O seu usuário é: "+ str(user_id))
	print("Usuário cadastrado com sucesso")
else:
	print("Email ja cadastrado")

