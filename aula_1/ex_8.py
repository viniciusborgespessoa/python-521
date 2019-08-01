import sys
import os
import flask


app = flask.Flask(__name__)

@app.route('/')

def get_index():
	return 'hello, world2'


@app.route('/users', methods=[ 'GET'])
def get_users():
	return 'users'

@app.route('/users', methods=[ 'POST'])
def post_users():
	return 'post users'

@app.route('/users/<int:user_id>', methods=[ 'GET'])
def get_users_by_id(user_id):
	return 'get users ' + str(user_id)

if __name__ == '__main__':

	current_module = os.path.abspath(os.path.curdir)
	sys.path.append(current_module)

	os.environ['FLASK_ENV'] = 'development'
	os.environ['FLASK_APP'] = 'ex_8.py'

	app.run(host='0.0.0.0', debug=True)