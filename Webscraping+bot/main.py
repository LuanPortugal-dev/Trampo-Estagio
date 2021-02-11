#from filters import FilterAwesome
from webscraping import resultado, resultado2
from telegram.ext import Updater, MessageHandler
import logging
import telegram

#log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#bot
bot = telegram.Bot(token='1631698693:AAFgFwFGXo4igPFeiB79fi3StFFQI6yZwNE')


#Mensagem
mensagem = (f'Resultados futuros dólar: {resultado}; \nResultados futuros bovespa: {resultado2}')

#enviar msg
def enviarMsg():    
    bot.send_message(chat_id=-1001331003161, text= mensagem)

enviarMsg()
