import telepot
bot = telepot.Bot("5208033687:AAHWZTn-K8JMzq-xi2BIfwGRIM_PDZoaUBE")

# criando uma função que será chamada toda a vez que recebermos uma mensagem
def recebendo_mensagem(msg):
    print(msg['text'])

bot.message_loop(recebendo_mensagem)

while True:
    pass