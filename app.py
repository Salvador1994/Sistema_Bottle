from bottle import route, run
from bottle import request, template
from bottle import static_file, get
from bottle import error
import  os

# static routes
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='static/css')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='static/js')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
	return static_file(filename, root='static/fonts')

@route('/login') # @get('/login')
def login():
	return template('login')

def check_login(username, password):
	dic = {'marcos':'python', 'Salvador Bila':'java'}
	if username in dic.keys() and dic[username] == password:
		return True
	return False

@route('/')
def index():
	return template('index')

@route('/index')
def index():
	return template('index')

@route('/login', method='POST') # @post('/login')
def acao_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	if check_login(username, password):
		return template('Area_Administrativa', sucesso=check_login(username, password), nome=username)
	else:
		return template('verificacao_login', sucesso=check_login(username, password), nome=username)

@error(404)
def error404(error):
	return template('pagina404')

if __name__ == '__main__':
	if os.environ.get('APP_LOCATION') == 'heroku':
		run(host='0.0.0.0',port=int(os.environ.get('PORT', 5000)))
	else:
		run(host='localhost', port=8080, debug=True, reloader=True)