import bottle

@bottle.route('/')
def home_page():
	return 'Hello World\n'

@bottle.route('/testpage')
def test_page():
	return 'this is a test page'

bottle.debug(True)
bottle.run(host='0.0.0.0', port=8080)
