#handler_bot.py
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

BOT_TOKEN='672768316:AAHXpYmnMzGp_eH0i-juikUFU6q9y78CBhA'

updater = Updater( token=BOT_TOKEN, use_context=True )
dispatcher = updater.dispatcher

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()