from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import logging

BOT_TOKEN='672768316:AAHXpYmnMzGp_eH0i-juikUFU6q9y78CBhA'

updater = Updater( token=BOT_TOKEN, use_context=True )
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="작업을 시작합니다.\nargs: {}, {}".format( type(context.args), context.args ))

def stop(update, context):
    logging.info( context.args )
    context.bot.send_message(chat_id=update.effective_chat.id, text="작업을 중단합니다.")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

start_handler = CommandHandler('start', start)
stop_handler = CommandHandler('stop', stop)
echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()