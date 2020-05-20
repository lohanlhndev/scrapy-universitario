import telepot
from cass import Invocador

bot_api = '1024907305:AAEI-WaIW4z3KlYv10V4u3DauBtGVHBmZE8' 



def receber(msg):
    text = msg['text']
    _id = msg['from']['id']
    invocador = Invocador(text)
    tele.sendMessage(_id, str(invocador.rank()))
    print(msg)

tele = telepot.Bot(bot_api)
tele.message_loop(receber)

while True:
    pass
