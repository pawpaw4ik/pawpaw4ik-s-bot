import telebot
import config
import random


API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я - робот инвалид, ненужный своему хозяину!
Я здесь для того чтобы мой хозяин научился писать код сложнее print('hello world')\
""")



@bot.message_handler(commands=['coin'])
def tossCoin(message):
    r = random.choice(['орел','решка'])
    bot.reply_to(message, f'{r}')

facts =['Среднее облако весит порядка 500 тонн, столько же весят 80 слонов.',
        'Самая крупная жемчужина в мире достигает 6 килограммов в весе.',
        'В Ирландии никогда не было кротов.',
        'Скорость распространения лавы после извержения, близка к скорости бега гончей.',
        'Существует пробирка, диаметр которой, в 10000 раз меньше диаметра человеческого волоса.',
        'У медуз нет мозгов и кровеносных сосудов.',
        'Кошки спят больше половины своей жизни.',
        'Лимон содержит больше сахара, чем клубника.',
        'В мире всего 7% левшей',
        'Алмазы могут гореть.',
        'У жирафа и человека одинаковое количество шейных позвонков.',
        'Страусы развивают скорость до 70 км в час.'
        ]

@bot.message_handler(commands=['fact'])
def fact(message):
    r = random.choice(facts)
    bot.reply_to(message, f'Случайный интересный факт:\n{r}')

bot.infinity_polling()