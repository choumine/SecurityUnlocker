from bottle import run,route,template,request
from unlockerInsert import UnlockerInsert
from unlockerSelect import UnlockerSelect
from unlockerPush import UnlockerPush

@route("/", method = 'get')
def index():
    return template('index')

@route('/', method = 'post')
def index():
    imei = request.forms.get('imei')
    timestamp = request.forms.get('timestamp')
    UnlockerPush(imei, timestamp)
    return UnlockerInsert(imei, timestamp)

@route('/view')
def view():
    return UnlockerSelect()

run(host = '172.17.176.81', port = 8888)