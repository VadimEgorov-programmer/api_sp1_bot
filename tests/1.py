import telegram

TELEGRAM_TOKEN = '1257430502:AAHbA1YG_HkePQnHltxd2H-osLCSL6Sdv2c'  # добавить токен
CHAT_ID = '1350087636'  # добавить chat_id


def send_message(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    return bot.send_message(chat_id=CHAT_ID, text=message)
send_message("Привет, я ботик, у меня баги")

# 1257430502:AAE2CdaRhiSxphI85L8x-W0cGfNTgZyH5wY