import telebot
from telebot import types
from config import token

bot = telebot.TeleBot(token)

previous_section = 'start'


class Keyboard:

    def __init__(self, message):
        self.message = message

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
            """Сейчас у всех полно проблем из-за мальца по имени Коронавирус, 
        и если у тебя тоже, или ты просто хочешь быть ко всему готов,
        то во вкладке F.A.Q. ты можешь найти кучу полезной информации.
            Во вкладке Stat ты можешь найти статистику по заражениям как 
        во всём мире, так и в России - будь в курсе событий!
            Во вкладке Профилактика можно узнать о мерах профилактики, 
        ведь никто не хочет заразиться или заразить близких, верно?""")   # Объяснение секций выбора
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
        text = ("""Заразилось: 8672 (+1175 за сутки)
        Выздоровело: 580 (+86 за сутки)
        Умерло: 63 (+5 за сутки)""")
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def moscow_keyboard(self):
        global previous_section
        previous_section = 'stat_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(back_button, step_back_button)
        text = ("""Заразилось: 5841 (+680 за сутки)
        Выздоровело: 270 (+48 за сутки)
        Умерло: 31 (+2 за сутки)""")
        bot.send_message(self.message.from_user.id, text, reply_markup=markup)

    def world_keyboard(self):
        global previous_section
        previous_section = 'stat_keyboard()'

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        step_back_button = types.KeyboardButton('Назад')
        markup.row(back_button, step_back_button)
        text = ("""Заразилось: 1.4 млн. (+86518 за сутки)
        Выздоровело: 308 тыс. (+15991 за сутки)
        Умерло: 83 тыс. (+7176 за сутки)""")
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
        text = 'illness'
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
