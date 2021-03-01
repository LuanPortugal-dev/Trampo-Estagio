#from filters import FilterAwesome

import logging
import telegram
import conexao
import pandas as pd

con = conexao.enviar_dados(con)

#log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#bot
bot = telegram.Bot(token='1631698693:AAFgFwFGXo4igPFeiB79fi3StFFQI6yZwNE')


#Mensagem
mensagem = pd.read_sql ("""SELECT pdf_cadastro FROM nome, cpf, email, telefone ;""", con = con)

#enviar msg
def enviarMsg():    
    bot.send_message(chat_id=-1001331003161, text= mensagem)

enviarMsg()
