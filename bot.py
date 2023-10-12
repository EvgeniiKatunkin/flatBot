import config
import content
import telebot

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def send_help(message):
    """The handler for /start and /help command"""
    bot.send_message(message.chat.id, "Hi, " + message.from_user.first_name + "! I'll show you all available options.",
                     reply_markup=config.keyboard(content.main_menu))


bot.infinity_polling()
