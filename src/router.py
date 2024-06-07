import telebot
import json
from dao import get_dataset_labels
from config import setings



bot = telebot.TeleBot(setings.BOT_TOKEM)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    arg = json.loads(message.text)
    result = get_dataset_labels(**arg)
    bot.send_message(message.chat.id, json.dumps(result))
  


bot.polling(none_stop=True)