import telebot
from telebot import types
from config import token
import requests

from bs4 import BeautifulSoup
# from lxml import html

bot = telebot.TeleBot(token)

previous_section = 'start'


class Keyboard:

    def __init__(self, message):
        self.message = message

    def get_mos_stats(self):
        html = requests.get('https://coronavirus-monitor.info/country/russia/moskva/').text
        soup = BeautifulSoup(html, 'lxml')

        mos_infected = soup.find('div', class_='info_blk stat_block confirmed').find('h2').text.split('+')[0][8::]
        mos_cured = soup.find('div', class_='info_blk stat_block cured').find('h2').text.split('+')[0][8::]
        mos_dead = soup.find('div', class_='info_blk stat_block deaths').find('h2').text.split('+')[0][7::]

        try:
            mos_infected_sup = soup.find('div', class_='info_blk stat_block confirmed').find('sup').text
        except Exception:
            mos_infected_sup = '+0'

        try:
            mos_cured_sup = soup.find('div', class_='info_blk stat_block cured').find('sup').text
        except Exception:
            mos_cured_sup = '+0'

        try:
            mos_dead_sup = soup.find('div', class_='info_blk stat_block deaths').find('sup').text
        except Exception:
            mos_dead_sup = '+0'

        mos_infected = 'Заражено: ' + mos_infected + ' ({} за сутки)'.format(mos_infected_sup)
        mos_cured = 'Вылечено: ' + mos_cured + ' ({} за сутки)'.format(mos_cured_sup)
        mos_dead = 'Погибло: ' + mos_dead + ' ({} за сутки)'.format(mos_dead_sup)

        return mos_infected, mos_cured, mos_dead

    def get_rus_stats(self):
        html = requests.get('https://coronavirus-monitor.info/country/russia/').text
        soup = BeautifulSoup(html, 'lxml')

        rus_infected = soup.find('div', class_='info_blk stat_block confirmed').find('h2').text.split('+')[0][8::]
        rus_cured = soup.find('div', class_='info_blk stat_block cured').find('h2').text.split('+')[0][8::]
        rus_dead = soup.find('div', class_='info_blk stat_block deaths').find('h2').text.split('+')[0][7::]

        try:
            rus_infected_sup = soup.find('div', class_='info_blk stat_block confirmed').find('sup').text
        except Exception:
            rus_infected_sup = '+0'

        try:
            rus_cured_sup = soup.find('div', class_='info_blk stat_block cured').find('sup').text
        except Exception:
            rus_cured_sup = '+0'

        try:
            rus_dead_sup = soup.find('div', class_='info_blk stat_block deaths').find('sup').text
        except Exception:
            rus_dead_sup = '+0'

        rus_infected = 'Заражено: ' + rus_infected + ' ({} за сутки)'.format(rus_infected_sup)
        rus_cured = 'Вылечено: ' + rus_cured + ' ({} за сутки)'.format(rus_cured_sup)
        rus_dead = 'Погибло: ' + rus_dead + ' ({} за сутки)'.format(rus_dead_sup)

        return rus_infected, rus_cured, rus_dead

    def get_world_stats(self):
        html = requests.get('https://coronavirus-monitor.info/#stats').text
        soup = BeautifulSoup(html, 'lxml')

        world_infected = soup.find('div', class_='info_blk stat_block confirmed').find('h2').text.split('+')[0][8::]
        world_cured = soup.find('div', class_='info_blk stat_block cured').find('h2').text.split('+')[0][8::]
        world_dead = soup.find('div', class_='info_blk stat_block deaths').find('h2').text.split('+')[0][7::]

        try:
            world_infected_sup = soup.find('div', class_='info_blk stat_block confirmed').find('sup').text
        except Exception:
            world_infected_sup = '+0'

        try:
            world_cured_sup = soup.find('div', class_='info_blk stat_block cured').find('sup').text
        except Exception:
            world_cured_sup = '+0'

        try:
            world_dead_sup = soup.find('div', class_='info_blk stat_block death').find('sup').text
        except Exception:
            world_dead_sup = '+0'

        world_infected = 'Заражено: ' + world_infected + ' ({} за сутки)'.format(world_infected_sup)
        world_cured = 'Вылечено: ' + world_cured + ' ({} за сутки)'.format(world_cured_sup)
        world_dead = 'Погибло: ' + world_dead + ' ({} за сутки)'.format(world_dead_sup)

        return world_infected, world_cured, world_dead

    def start_keyboard(self):
        global previous_section
        previous_section = 'start'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        faq_button = types.KeyboardButton('F.A.Q.')
        stat_button = types.KeyboardButton('Stat')
        prof_button = types.KeyboardButton('Профилактика')
        # markup.ResizeKeyboard = True
        markup.row(faq_button, stat_button)
        markup.row(prof_button)
        text = (
            """    Сейчас у всех полно проблем из-за мальца по имени Коронавирус, 
и если у тебя тоже, или ты просто хочешь быть ко всему готов,
то во вкладке F.A.Q. ты можешь найти кучу полезной информации.
    Во вкладке Stat ты можешь найти статистику по заражениям как 
во всём мире, так и в России - будь в курсе событий!
    Во вкладке Профилактика можно узнать о мерах профилактики, 
ведь никто не хочет заразиться или заразить близких, верно?""")  # Объяснение секций выбора
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def faq_button_keyboard(self):
        global previous_section
        previous_section = 'start_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        sick_button = types.KeyboardButton('Заболевание')
        symptoms_button = types.KeyboardButton('Симптомы')
        miscellaneous_button = types.KeyboardButton('Прочее')
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(sick_button, symptoms_button, miscellaneous_button)
        markup.row(back_button, step_back_button)
        text = 'Выбери интересную секцию.'
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def stat_keyboard(self):
        global previous_section
        previous_section = 'start_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        russia_button = types.KeyboardButton('По России')
        world_button = types.KeyboardButton('По миру')
        moscow_button = types.KeyboardButton('По Москве')
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(russia_button, world_button, moscow_button)
        markup.row(back_button, step_back_button)
        text = 'Выбери раздел статистики.'
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def russia_keyboard(self):
        global previous_section
        previous_section = 'stat_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(back_button, step_back_button)
        text = ('\n'.join(self.get_rus_stats()))
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def moscow_keyboard(self):
        global previous_section
        previous_section = 'stat_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(back_button, step_back_button)
        text = ('\n'.join(self.get_mos_stats()))
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def world_keyboard(self):
        global previous_section
        previous_section = 'stat_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(back_button, step_back_button)
        text = ('\n'.join(self.get_world_stats()))
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def miscellaneous_keyboard(self):
        global previous_section
        previous_section = 'faq_button_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(back_button, step_back_button)
        text = ("""    Куда звонить, если у меня есть прочие вопросы касательно коронавируса, 
мне нужна помощь с карантином, или есть подозрения на заболевание? 
Горячая линия по коронавирусу - +7 (495) 870-45-09 (ежедневно, с 8:00 до 21:00), 
там можно уточнить любую информацию о COVID-19, также в Москве могут помочь с доставкой продуктов и лекарств
пенсионерам и горожанам с хроническими заболеваниями.

    Зачем нужен карантин?
Карантин - необходимая мера по снижению контактов среди населения, что значительно уменьшает 
количество заражённых. Более того, в странах, где по тем или иным причинам карантин соблюдается строже
статистика заражений заметно просела. Даже если вы обладаете отличным иммунитетом, или если 
вы не боитесь заразиться, вы обязаны соблюдать карантин, чтобы не распространять вирус, ведь, учитывая длинный 
так называемый инкубационный период, в случае заражения человек становится заразным раньше, чем замечает это.

    Помогают ли медицинские маски?
Обычные медицинские маски помогают вам не заражать окружающих, ведь вы можете не знать, заразны ли вы. 
Также нереспираторные маски защищают от прямого контакта с крупными объектами такими как слюна заражённого.
Однако, при возможности рекомендуется использовать гиппоалергенные респираторные маски, они 
способны фильтровать воздух и даже задерживать сами часицы вируса, несмотря на их микроскопический размер.
Напоминаем, что не стоит носить одноразовые маски дольше того времени, на которое они рассчитаны, это
лишь повысит риск заражения.

    Как узнать, вхожу ли я в группу риска?
Группы риска составляют следующие категории людей:
1. люди, проживающие с заболевшим коронавирусом;
2. пациенты с диагнозом «пневмония»;
3. люди, проживающие с пациентами с диагнозом «пневмония»;
4. пациенты с симптомами ОРВИ старше 60 лет или имеющие сопутствующую хроническую патологию 
(сердечно-сосудистые заболевания, сахарный диабет, онкологические заболевания, заболевания эндокринной системы);
5. пациенты с симптомами ОРВИ.

    До какого числа действует режим самоизоляции?
Для профилактики распространения COVID-19 в Москве продлят все введенные ранее ограничения до 1 мая.

    Куда я могу ходить?
Можно покидать дома по естественным нуждам: поход в ближайший магазин или аптеку, вынос мусора, выгул питомца 
в радиусе 100 метров от дома. В гипермаркет можно поехать на личном автомобиле или на такси.

    Будут ли вводиться пропуска?
На текущей момент ответ - нет, однако, со слов мэра Москвы Собянина, к этому вопросу могут вернутся в случае
неблагоприятного развития эпидемиологической ситуации или увеличения количества нарушений режима самоизоляции.

    Нужно ли носить с собой паспорт?
Необходимо иметь при себе любой документ, подтверждающий личность, вот список таких документов:
паспорт, свидетельство о рождении (для лиц младше 14 лет), удостоверение личности моряка, 
дипломатический паспорт, удостоверение личности военнослужащего, удостоверение беженца, военный билет, 
служебное удостоверение (для работников прокуратуры), заграничный паспорт, вид на жительство.
        """)

        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def symptoms_keyboard(self):
        global previous_section
        previous_section = 'faq_button_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(back_button, step_back_button)
        text = ("""боль в горле,
кашель,
чихание,
повышение температуры тела,
дыхательная недостаточность (при тяжелом течении)""")
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def illness_keyboard(self):
        global previous_section
        previous_section = 'faq_button_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(back_button, step_back_button)
        text = ("""Коронавирусная инфекция COVID-19 характеризуется легким течением с такими симптомами как боль 
в горле, кашель и повышение температуры тела. У некоторых людей болезнь может протекать в более тяжелой форме 
и приводить к пневмонии или дыхательной недостаточности. В более редких случаях болезнь может иметь летальный исход. 
Пожилые люди и люди с определенными заболеваниями (например, астмой, диабетом или патологией сердца), подвержены 
повышенному риску развития тяжелых форм коронавирусной инфекции.
Новая коронавирусная инфекция относится к острым респираторным вирусным инфекциям (ОРВИ), и осложнения у нее могут 
быть такие же, как и у других ОРВИ: пневмония, бронхит, синусит и другие.
""")
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def prophylaxis_keyboard(self):
        global previous_section
        previous_section = 'start_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(back_button, step_back_button)
        text = (""" Если вы и правда не хотите заболеть коронавирусом, то первое о чём стоит задуматься - 
меры профилактики, тем более, что они довольно просты :)
    1) Следите за чистотой рук, особенно если вы часто покидаете дом. Старайтесь как можно реже касаться лица.
Когда кашляете или чихаете, старайтесь закрывать нос и рот одноразовой салфеткой, если её нет под рукой, 
прикрывайтесь локтем - это безопасней, чем ладонью или кулаком.
    2) Старайтесь избегать контакта с пожилыми людьми. Желательно не только с пожилыми, просто у них 
в среднем куда более ослабленный иммунитет и они уже в группе риска за счёт своего возраста.
    3) Купите хороший антисептик для рук - такой, чтобы вам было комфортно использовать его на регулярной основе. 
    4) Старайтесь как можно меньше касаться всего, чего, вероятно, уже кто-то касался, в особенности - еды.
    5) В общественных местах держите дистанцию хотя бы в 1.5 метра.
    6) На работе и в автомобиле (а лучше и дома) регулярно очищайте поверхности к которым вы прикасаетесь.
    7) Проветривайте все помещения, в которых вы проводите значительное количество времени.
    8) И самое главное - оставайтесь дома, берегите себя и своих близких. :)""")
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)
