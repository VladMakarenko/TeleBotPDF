import telebot
import fitz
import os

bot = telebot.TeleBot('5971771120:AAGaqrS8-p59lRXP0qNk-2Oqd22Ck7Lt8bo')


@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Для початку роботи перетягніть або загрузіть сюди PDF файл")


@bot.message_handler(content_types=['document'])
def get_text_pdf(message):
    try:
        chat_id = message.chat.id

        basedir = os.path.abspath(os.getcwd())

        src = basedir[:-(len(basedir.split('\\')[-1]) + 1)]

        doc = fitz.open(f'{src}\\{message.document.file_name}')
        text = {}
        with fitz.open(doc) as doc:
            for num, page in enumerate(doc.pages()):
                text[num] = page.get_text()
            bot.send_message(chat_id, text[num])
    except Exception as ex:
        bot.reply_to(message, ex)


bot.polling(none_stop=True, interval=0)
