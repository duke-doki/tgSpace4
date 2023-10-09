import telegram
from environs import Env


env = Env()
env.read_env()
tg_token = env.str('TG_TOKEN')
bot = telegram.Bot(token=tg_token)
#print(bot.get_me())

#bot.send_message(text='Hi John!', chat_id='@tgspace4')

bot.send_document(chat_id='@tgspace4', document=open('images/epic1.png', 'rb'))
