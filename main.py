import telebot
import key
from telebot import types

bot = telebot.TeleBot(key.token)

@bot.message_handler(commands=["start"])
def keyboard_start(messadge):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    privet = types.KeyboardButton(text="Привет")
    startKboard.add(privet)
    bot.send_message(messadge.chat.id, "хайо!", reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="Привет")
def echo_all(messadge):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    ochae = types.KeyboardButton(text="поговорить о чае")
    startKboard.add(ochae)
    bot.send_message(messadge.chat.id, "о чём хочешь поболтать? :3", reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="поговорить о чае")
def echo_all(messadge):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    malinovi = types.KeyboardButton(text="малиновый чай")
    zeleniy = types.KeyboardButton(text="зеленый чай")
    startKboard.add(malinovi, zeleniy)
    bot.send_message(messadge.chat.id, "о каком чае хочешь послушать?", reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="малиновый чай")
def mch(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    cherniy = types.KeyboardButton(text="чай из шиповника")
    chernichny = types.KeyboardButton(text="клубничный чай")
    startKboard.add(cherniy, chernichny)
    bot.send_message(message.chat.id, 'вот о малиновом чае! " https://teawiki.ru/chai/malinovyj-polza-i-vred/ "', reply_markup=startKboard)
    
@bot.message_handler(func=lambda m: m.text =="чай из шиповника")
def mch(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    cherniy = types.KeyboardButton(text="черный чай")
    chernichny = types.KeyboardButton(text="черничный чай")
    startKboard.add(cherniy, chernichny)
    bot.send_message(message.chat.id, 'вот о чае из шиповника! " https://zavarka.life/recepty/shipovnik.html "', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="клубничный чай")
def mch(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    cherniy = types.KeyboardButton(text="чай из голубики")
    chernichny = types.KeyboardButton(text="чай из рябины")
    startKboard.add(cherniy, chernichny)
    bot.send_message(message.chat.id, 'вот о клубничном чае! " https://cupstea.ru/chajnye-recepty/s-klubnikoy.html? "', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="чай из голубики")
def mch(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    cherniy = types.KeyboardButton(text="ромашковый чай")
    chernichny = types.KeyboardButton(text="чай с лимоном")
    startKboard.add(cherniy, chernichny)
    bot.send_message(message.chat.id, 'вот о чае из голубики! " https://hozyain.by/zdorovie/golubika-lekarstvo-ot-starosti/? "', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="ромашковый чай")
def mch(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    cherniy = types.KeyboardButton(text="ромашковый чай")
    chernichny = types.KeyboardButton(text="чай с лимоном")
    startKboard.add(cherniy, chernichny)
    bot.send_message(message.chat.id, 'вот о ромашковом чае! "https://ru.siberianhealth.com/ru/blogs/pitanie/kak-pit-romashkovyy-chay-s-polzoy/ "', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="чай с лимоном")
def mch(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    cherniy = types.KeyboardButton(text="чай из зверобоя")
    chernichny = types.KeyboardButton(text="лавандовый чай")
    startKboard.add(cherniy, chernichny)
    bot.send_message(message.chat.id, 'вот о чае с лимоном! "https://prochayok.ru/fruktovo-yagodnyj/chaj-s-limonom.html "', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="чай из зверобоя")
def mich(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    end2 = types.KeyboardButton(text="благодарю!")
    startKboard.add(end2)
    bot.send_message(message.chat.id, 'вот о чае из зверобоя!"https://chayguru.info/travyanoj-chaj/chaj-iz-zveroboya-polza-i-vred-dlya-organizma-pokazaniya-k-primeneniyu? ' , reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="лавандовый чай")
def mich(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    end = types.KeyboardButton(text="спасибо!")
    startKboard.add(end)
    bot.send_message(message.chat.id, 'вот о лавандовом чае!"https://polzavred-edi.ru/chaj-s-lavandoj-polza-i-vred-dlja-organizma/" ' , reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="чай из рябины")
def mch(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    cherniy = types.KeyboardButton(text="чай с имбирем")
    chernichny = types.KeyboardButton(text="чай с молоком")
    startKboard.add(cherniy, chernichny)
    bot.send_message(message.chat.id, 'вот о чае из рябины! " https://recepty-prirody.ru/narodnye-sredstva/otvary/chaj-iz-krasnoj-ryabiny.html "', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="чай с имбирем")
def mich(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    end2 = types.KeyboardButton(text="благодарю!")
    startKboard.add(end2)
    bot.send_message(message.chat.id, 'вот о чае с имбирем!"https://ashaindia.ru/kak-pravilno-zavarivat-chay-s-imbirem/" ' , reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="чай с молоком")
def mich(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    end = types.KeyboardButton(text="спасибо!")
    startKboard.add(end)
    bot.send_message(message.chat.id, 'вот о чае с молоком!"https://prochayok.ru/drugie-vidy-chaya/s-molokom.html" ' , reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="зеленый чай")
def zch(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    onchan = types.KeyboardButton(text="чай анчан")
    mint = types.KeyboardButton(text="мятный чай")
    startKboard.add(onchan, mint)
    bot.send_message(message.chat.id, 'вот о зеленом чае! "https://ru.wikipedia.org/wiki/%D0%97%D0%B5%D0%BB%D1%91%D0%BD%D1%8B%D0%B9_%D1%87%D0%B0%D0%B9" ', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="чай анчан")
def ach(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    end = types.KeyboardButton(text="спасибо!")
    startKboard.add(end)
    bot.send_message(message.chat.id, 'вот о чае ончан! "https://ru.wikipedia.org/wiki/%D0%9A%D0%BB%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D1%8F_%D1%82%D1%80%D0%BE%D0%B9%D1%87%D0%B0%D1%82%D0%B0%D1%8F" ', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="мятный чай")
def mich(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    end2 = types.KeyboardButton(text="благодарю!")
    startKboard.add(end2)
    bot.send_message(message.chat.id, 'вот о мятном чае!"https://zavarka.life/recepty/chaj-s-mjatoy.html" ' , reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="черный чай")
def mich(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    end2 = types.KeyboardButton(text="благодарю!")
    startKboard.add(end2)
    bot.send_message(message.chat.id, 'вот о черном чае!"https://ru.wikipedia.org/wiki/%D0%A7%D1%91%D1%80%D0%BD%D1%8B%D0%B9_%D1%87%D0%B0%D0%B9" ' , reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="черничный чай")
def mich(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    end = types.KeyboardButton(text="спасибо!")
    startKboard.add(end)
    bot.send_message(message.chat.id, 'вот о черничном чае!"https://tutknow.ru/meal/15259-chernichnyy-chay-polza-vred-zagotovka-syrja-recepty.html" ' , reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="благодарю!")
def mich(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id, 'пока-пока! чтобы снова запустить бота напишите "/start" <3', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="спасибо!")
def bye(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id, 'удачи! чтобы снова запустить бота напишите "/start" ;3', reply_markup=startKboard)


bot.polling()