from bottle import run,route,template,request

@route('/test')
def test():
    return 'Hello world!'

run(host = '49.7.144.4', port = 80)