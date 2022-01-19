import telebot
import random


bot = telebot.TeleBot("5036824626:AAH-dP5b7FjCvWc21uZzPOcNKVfiODBhLbs")
list=[0,1,2,3,4,5,6,7,8,9,'q','w','e','r','t','y','u','i','o','p','~','!','@','#','$','%','^','&','*']

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Hello!\nInput how long token should be..")

@bot.message_handler(content_types=['text'])
def rand_token(message):
    amount=message.text
    token=''
    try: 
        for z in range(int(amount)):
            rand_symdol=random.choice(list)
            token+=f'{rand_symdol}'
        bot.reply_to(message, token)
    except ValueError:
        bot.send_message(message.chat.id, "Sorry mate, workind only with nubers..")
bot.infinity_polling()