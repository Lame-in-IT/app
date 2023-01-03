from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('🪆 Главное меню')
btnBackMarcet = KeyboardButton('🔙 Маркетплейсы')

# --- Main Menu ---
btnprice = KeyboardButton('🅿️ Данные Маркетплейсов')
btnreviews = KeyboardButton('📯 Отзывы на WB')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnprice, btnreviews)


# --- Menu Price --- 
btnPriceAll = KeyboardButton('Изменения в ценах')
evrifung = KeyboardButton('🅿️ Поставки')
mainPrice = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPriceAll, evrifung, btnMain)

# --- Menu Deliveries ---
btnOZON = KeyboardButton('Поставки на OZON')
btnWB = KeyboardButton('Поставки на WB')
btnYM = KeyboardButton('Поставки на Яндекс')
btnBackDeliv = KeyboardButton('🔙 Назад к разделам')
mainDeliveries = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOZON, btnWB, btnYM, btnBackDeliv)

# --- Menu Deliveries OZON ---
btnOZON_1week = KeyboardButton('OZON поставки на 2 недели')
btnOZON_2week = KeyboardButton('OZON поставки на 4 недели')
btnOZON_3week = KeyboardButton('OZON поставки на 6 недели')
btnOZON_3month = KeyboardButton('OZON поставки на 2 месяца')
mainDelivOZON = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOZON_1week, btnOZON_2week, btnOZON_3week, btnOZON_3month, btnBackMarcet)

# --- Menu Deliveries WB ---
btnWB_1week = KeyboardButton('WB поставки на 2 недели')
btnWB_2week = KeyboardButton('WB поставки на 4 недели')
btnWB_3week = KeyboardButton('WB поставки на 6 недели')
btnWB_3month = KeyboardButton('WB поставки на 2 месяца')
mainDelivWB = ReplyKeyboardMarkup(resize_keyboard=True).add(btnWB_1week, btnWB_2week, btnWB_3week, btnWB_3month, btnBackMarcet)

# --- Menu Deliveries YM ---
btnYM_1week = KeyboardButton('Яндекс поставки на 2 недели')
btnYM_2week = KeyboardButton('Яндекс поставки на 4 недели')
btnYM_3week = KeyboardButton('Яндекс поставки на 6 недели')
btnYM_3month = KeyboardButton('Яндекс поставки на 2 месяца')
mainDelivYM = ReplyKeyboardMarkup(resize_keyboard=True).add(btnYM_1week, btnYM_2week, btnYM_3week, btnYM_3month, btnBackMarcet)