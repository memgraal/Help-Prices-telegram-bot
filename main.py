from telebot import TeleBot
from telebot import types
from telebot.types import Message
from products import Perecrestok, SevenSteps


bot = TeleBot(token = "6611539409:AAFc2AgxMZc-LnsHXnuVMYQR98p4vXFGAyo")


@bot.message_handler(commands = ['start', 'hello'])
def start(message : Message) -> None:
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    markup.row("Показать категории товаров")

    bot.send_message(chat_id = message.chat.id,
                    text = f"""Здравствуйте, {message.from_user.first_name}, этот бот создан для того, чтобы находить выгодные\nпредложения на товары в популярных магазинах Cанкт-Петербурга""", 
                    reply_markup = markup)


@bot.message_handler(regexp = "Показать категории товаров")
def Show_categories(message : Message) -> None:
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    markup.row("Молоко"); markup.row("Сыр"); markup.row("Хлеб"); markup.row("Картошка")
    
    bot.send_message(chat_id = message.chat.id,
                    text = "Выберите одну из категорий",
                    reply_markup = markup)

@bot.message_handler(regexp = "Назад")
def get_back(message : Message) -> None:
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    markup.row("Показать категории товаров")
    bot.send_message(chat_id = message.chat.id,
                    text = "💥",
                    reply_markup = markup)

@bot.message_handler(regexp = "Молоко")
def milk(message : Message) -> None:
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    markup.row("Назад")
    
    #                                      МАГАЗИН  ПЕРЕКРЕСТОК
    bot.send_message(chat_id = message.chat.id,
                        text = "*Магазин : Перекресток*",
                        reply_markup = markup,
                        parse_mode='Markdown')
        
    for counter, product in enumerate(Perecrestok().P_Parse_milk()[::-1]):        # в телеграм боте пользователь может увидеть только 4 первых предложений 
        if counter >= 4: break

        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text = "Перейти на сайт магазина", url = f"https://spb.perekrestok.ru{product[2]}")
        keyboard.add(url_button)

        bot.send_photo(chat_id = message.chat.id,
                        photo = f"{product[3]}",
                        caption = f"""{product[0][0]}\n
                            Магазин : Перекресток
                            {product[1][0]} : {product[1][1]}""",
                        reply_markup = keyboard)
            
    #                                      МАГАЗИН 7ШАГОФФ

    bot.send_message(chat_id = message.chat.id,
                        text = "*Магазин : 7шагофф*",
                        parse_mode='Markdown')
        
    for counter, product in enumerate(SevenSteps().S_Parse_milk()):        # в телеграм боте пользователь может увидеть только 4 первых предложений 
        if counter >= 3: break

        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на сайт магазина", url = f"https://semishagoff.org{product[2]}")
        keyboard.add(url_button)

        bot.send_photo(chat_id = message.chat.id,
                        photo = f"https://semishagoff.org{product[3]}",
                        caption = f"""{product[0]}\n
                        Магазин : 7шагофф
                        Цена : {product[1]}""",
                        reply_markup = keyboard)

@bot.message_handler(regexp = "Сыр")
def cheese(message : Message) -> None:
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    markup.row("Назад")
    
    #                                      МАГАЗИН  ПЕРЕКРЕСТОК
    bot.send_message(chat_id = message.chat.id,
                        text = "*Магазин : Перекресток*",
                        reply_markup = markup,
                        parse_mode='Markdown')
        
    for counter, product in enumerate(Perecrestok().P_Parse_cheese()[::-1]):        # в телеграм боте пользователь может увидеть только 4 первых предложений 
        if counter >= 4: break

        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text = "Перейти на сайт магазина", url = f"https://spb.perekrestok.ru{product[2]}")
        keyboard.add(url_button)

        bot.send_photo(chat_id = message.chat.id,
                        photo = f"{product[3]}",
                        caption = f"""{product[0][0]}\n
                        Магазин : Перекресток
                        {product[1][0]} : {product[1][1]}""",
                        reply_markup = keyboard)
            
    #                                      МАГАЗИН 7ШАГОФФ

    bot.send_message(chat_id = message.chat.id,
                        text = "*Магазин : 7шагофф*",
                        parse_mode='Markdown')
        
    for counter, product in enumerate(SevenSteps().S_Parse_cheese()):        # в телеграм боте пользователь может увидеть только 4 первых предложений 
        if counter >= 3: break

        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на сайт магазина", url = f"https://semishagoff.org{product[2]}")
        keyboard.add(url_button)

        bot.send_photo(chat_id = message.chat.id,
                        photo = f"https://semishagoff.org{product[3]}",
                        caption = f"""{product[0]}\n
                        Магазин : 7шагофф
                        Цена : {product[1]}""",
                        reply_markup = keyboard)

@bot.message_handler(regexp = "Хлеб")
def bread(message : Message) -> None:
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    markup.row("Назад")
    
    #                                      МАГАЗИН  ПЕРЕКРЕСТОК
    bot.send_message(chat_id = message.chat.id,
                        text = "*Магазин : Перекресток*",
                        reply_markup = markup,
                        parse_mode='Markdown')
        
    for counter, product in enumerate(Perecrestok().P_Parse_bread()[::-1]):        # в телеграм боте пользователь может увидеть только 4 первых предложений 
        if counter >= 4: break

        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text = "Перейти на сайт магазина", url = f"https://spb.perekrestok.ru{product[2]}")
        keyboard.add(url_button)

        bot.send_photo(chat_id = message.chat.id,
                        photo = f"{product[3]}",
                        caption = f"""{product[0][0]}\n
                        Магазин : Перекресток
                        {product[1][0]} : {product[1][1]}""",
                        reply_markup = keyboard)
            
    #                                      МАГАЗИН 7ШАГОФФ

    bot.send_message(chat_id = message.chat.id,
                        text = "*Магазин : 7шагофф*",
                        parse_mode='Markdown')
        
    for counter, product in enumerate(SevenSteps().S_Parse_bread()):        # в телеграм боте пользователь может увидеть только 4 первых предложений 
        if counter >= 3: break

        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на сайт магазина", url = f"https://semishagoff.org{product[2]}")
        keyboard.add(url_button)

        bot.send_photo(chat_id = message.chat.id,
                        photo = f"https://semishagoff.org{product[3]}",
                        caption = f"""{product[0]}\n
                        Магазин : 7шагофф
                        Цена : {product[1]}""",
                        reply_markup = keyboard)

@bot.message_handler(regexp = "Картошка")
def potato(message : Message) -> None:
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    markup.row("Назад")
    
    #                                      МАГАЗИН  ПЕРЕКРЕСТОК
    bot.send_message(chat_id = message.chat.id,
                        text = "*Магазин : Перекресток*",
                        reply_markup = markup,
                        parse_mode='Markdown')
        
    for counter, product in enumerate(Perecrestok().P_Parse_potato()[::-1]):        # в телеграм боте пользователь может увидеть только 5 первых предложений 
        if counter >= 4: break

        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text = "Перейти на сайт магазина", url = f"https://spb.perekrestok.ru{product[2]}")
        keyboard.add(url_button)

        bot.send_photo(chat_id = message.chat.id,
                        photo = f"{product[3]}",
                        caption = f"""{product[0][0]}\n
                        Магазин : Перекресток
                        {product[1][0]} : {product[1][1]}""",
                        reply_markup = keyboard)
            
    #                                      МАГАЗИН 7ШАГОФФ

    bot.send_message(chat_id = message.chat.id,
                        text = "*Магазин : 7шагофф*",
                        parse_mode='Markdown')
        
    for counter, product in enumerate(SevenSteps().S_Parse_potato()):        # в телеграм боте пользователь может увидеть только 4 первых предложений 
        if counter >= 3: break

        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на сайт магазина", url = f"https://semishagoff.org{product[2]}")
        keyboard.add(url_button)

        bot.send_photo(chat_id = message.chat.id,
                        photo = f"https://semishagoff.org{product[3]}",
                        caption = f"""{product[0]}\n
                        Магазин : 7шагофф
                        Цена : {product[1]}""",
                        reply_markup = keyboard)

bot.polling(non_stop = True)