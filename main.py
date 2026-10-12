import os
import telebot

TOKEN = "ضع_توكن_البوت_هنا"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بك! يعمل البوت بنجاح عبر الاستضافة السحابية.")

bot.infinity_polling()
