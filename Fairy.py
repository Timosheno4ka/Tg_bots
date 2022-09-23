#5540443440:AAEiCxW3OzAdA0ykM479N7p8PgfNMbtf7hA

import telebot
from telebot import types

token = '5540443440:AAEiCxW3OzAdA0ykM479N7p8PgfNMbtf7hA'
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    colob_btn = types.InlineKeyboardButton(text="Колобок", callback_data='1')
    repka_btn = types.InlineKeyboardButton(text="Репка", callback_data='2')
    keyboard.add(colob_btn)
    keyboard.add(repka_btn)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = create_keyboard()
    bot.send_message(
        message.chat.id,
        "Здравствуйте! Выберите сказку: ",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data == '1':
            img = open('Colobok.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption= "Жил-был старик со старухою. Просит старик:— Испеки, старуха, колобок! "
                         "— Из чего печь — то? Муки нету, — отвечает ему старуха. "
                         "— Э — эх, старуха! По коробу поскреби, по сусеку помети; авось муки и наберется.")
            img.close()
            img = open('grandmother.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Взяла старуха крылышко, по коробу поскребла, по сусеку помела, и набралось муки пригоршни с две. "
                        "Замесила на сметане, изжарила в масле и положила на окошечко постудить.Колобок полежал — полежал, да вдруг и покатился — с окна на лавку, "
                        "с лавки на пол, по полу да к дверям, перепрыгнул через порог в сени, из сеней на крыльцо, с крыльца — на двор, со двора за "
                        "ворота, дальше и дальше.")
            img.close()
            img = open('hare.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Катится колобок по дороге, а навстречу ему заяц: — Колобок, колобок! Я тебя съем."
                        "— Не ешь меня, косой зайчик! Я тебе песенку спою, — сказал колобок и запел: "
                        "Я Колобок, Колобок! Я по коробу скребен, По сусеку метен, На сметане мешон, "
                        "Да в масле пряжон, На окошке стужон; Я от дедушки ушел, Я от бабушки ушел, "
                        "И от тебя, зайца, не хитро уйти! И покатился себе дальше; только заяц его и видел!")
            img.close()
            img = open('wolf.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Катится колобок по дороге, а навстречу ему волк: — Колобок, колобок! Я тебя съем."
                        "— Не ешь меня, волк! Я тебе песенку спою, — сказал колобок и запел: "
                        "Я Колобок, Колобок! Я по коробу скребен, По сусеку метен, На сметане мешон, "
                        "Да в масле пряжон, На окошке стужон; Я от дедушки ушел, Я от бабушки ушел, Я от зайца ушел,"
                        "И от тебя, волка, не хитро уйти! И покатился себе дальше; только волк его и видел!")
            img.close()
            img = open('bear.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Катится колобок по дороге, а навстречу ему медведь: — Колобок, колобок! Я тебя съем."
                        "— Не ешь меня, медведь! Я тебе песенку спою, — сказал колобок и запел: "
                        "Я Колобок, Колобок! Я по коробу скребен, По сусеку метен, На сметане мешон, "
                        "Да в масле пряжон, На окошке стужон; Я от дедушки ушел, Я от бабушки ушел, Я от зайца ушел,Я от волка ушел,"
                        "И от тебя, медведя, не хитро уйти! И покатился себе дальше; только медведь его и видел!")
            img.close()
            img = open('fox.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Катится колобок по дороге, а навстречу ему лиса: — Колобок, колобок! Я тебя съем."
                        "— Не ешь меня, лиса! Я тебе песенку спою, — сказал колобок и запел: "
                        "Я Колобок, Колобок! Я по коробу скребен, По сусеку метен, На сметане мешон, "
                        "Да в масле пряжон, На окошке стужон; Я от дедушки ушел, Я от бабушки ушел, Я от зайца ушел,Я от волка ушел,Я от медведя ушел"
                        "А от тебя, лиса, и подавно уйду! — Какая славная песенка! — сказала лиса. — Но ведь я, колобок, стара стала, "
                        "плохо слышу; сядь-ка на мою мордочку да пропой еще разок погромче. Колобок вскочил лисе на мордочку и запел ту же песню."
                        "— Спасибо, колобок! Славная песенка, еще бы послушала! "
                        "Сядь-ка на мой язычок да пропой в последний разок, — сказала лиса и высунула свой язык; "
                        "колобок прыг ей на язык, а лиса — ам его! И съела колобка…",
            reply_markup= keyboard)
            img.close()
        elif call.data == '2':
            img = open('posadil.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption= "Посадил дед репку. Выросла репка большая-пребольшая.")
            img.close()
            img = open('tyanet.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Пошел дед репку рвать: тянет-потянет, вытянуть не может!")
            img.close()
            img = open('ded_babka.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Позвал дед бабку: бабка за дедку, дедка за репку — тянут-потянут, вытянуть не могут!")
            img.close()
            img = open('vny4ka.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Позвала бабка внучку: внучка за бабку, бабка за дедку, дедка за репку — тянут-потянут, вытянуть не могут!")
            img.close()
            img = open('zhy4ka.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Позвала внучка Жучку: Жучка за внучку, внучка за бабку, бабка за дедку, дедка за репку — "
                        "тянут-потянут, вытянуть не могут!")
            img.close()
            img = open('cat.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Позвала Жучка кошку: кошка за Жучку, Жучка за внучку, внучка за бабку, бабка за дедку, дедка за репку — "
                        "тянут-потянут, вытянуть не могут!")
            img.close()
            img = open('mouse.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Позвала кошка мышку: мышка за кошку, кошка за Жучку, Жучка за внучку, внучка за бабку, бабка за дедку,"
                        " дедка за репку —тянут-потянут, — вытянули репку!",
            reply_markup= keyboard)
            img.close()


if __name__ == "__main__":
    bot.polling(none_stop=True)
