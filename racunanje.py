import bottle
import model

potovanje = model.Potovanje('stanje.json')

potovanje = model.Potovanje()


@bottle.get('/')
def index():
    return bottle.template('index.tpl') 

#v brskalnik napisemo localhost:8080 in tam je kalkulator

@bottle.post('/novo_potovanje/') #delamo piškotek
def novo():
    novo = potovanje.novo_potovanje()
    bottle.response.set_cookie('novo', path='/')
    bottle.redirect('/potovanje/')

#post spreminja stanje, get pa ne
bottle.run(reloader=True, debug=True)