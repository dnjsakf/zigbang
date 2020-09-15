#dochis_bot.py
import telegram

BOT_TOKEN='672768316:AAHXpYmnMzGp_eH0i-juikUFU6q9y78CBhA'

bot = telegram.Bot( token=BOT_TOKEN )
chat_id = bot.getUpdates()[-1].message.chat.id

bot.sendMessage(chat_id=chat_id, text='[{}]안녕하세요, 도치봇입니다.'.format( chat_id ) )