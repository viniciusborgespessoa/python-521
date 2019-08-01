import sys
import os
import flask


app = flask.Flask(__name__)

@app.route('/')

def get_index():
	return 'hello, world'


if __name__ == '__main__':

	current_module = os.path.abspath(os.path.curdir)
	sys.path.append(current_module)

	os.environ['FLASK_ENV'] = 'development'
	os.environ['FLASK_APP'] = 'ex_8.py'
	
	app.run(host='0.0.0.0', debug=True)