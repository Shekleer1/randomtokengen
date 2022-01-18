import telebot
import random


bot = telebot.TeleBot("5036824626:AAH-dP5b7FjCvWc21uZzPOcNKVfiODBhLbs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "введи количество знаков в токене")

@bot.message_handler(content_types=['text'])
def gen_token(message):
    try:
        git=message.text
        token=''
        num=0
        symbols=[0,1,2,3,4,5,6,7,8,9,'q','w','e','r','t','y','u','i','o','p','~','!','@','#','$','%','^','&','*']
        while num!=int(git):
            symbols1=symbols.copy()
            random.shuffle(symbols1)
            rand_symbol=symbols1.pop()
            token+=str(rand_symbol)
            num+=1        
    except ValueError:
        bot.send_message(message.chat.id, 'введите число!')
    bot.reply_to(message, token)
bot.infinity_polling()