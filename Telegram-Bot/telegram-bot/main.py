import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from filters import FilterAwesome


filter_awesome = FilterAwesome()

#log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


#objeto principal e dispatcher
updater = Updater(token= '1631698693:AAFgFwFGXo4igPFeiB79fi3StFFQI6yZwNE', use_context=True)
dispatcher = updater.dispatcher


#func callback start
def start(update, context):
    context.bot.send_message(chat_id=-1001331003161, text=update.message.text)

#func callback echo
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

#func callback caps
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

#funções do bot
bot_handler = MessageHandler(filter_awesome, start)
dispatcher.add_handler(bot_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

updater.start_polling()
