from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('🪆 Главное меню')
btnBackMarcet = KeyboardButton('🔙 Маркетплейсы')
main = KeyboardButton('Меню')

# --- Main Menu ---
btnprice = KeyboardButton('🅿️ Данные Маркетплейсов')
btnreviews = KeyboardButton('📯 Отзывы на WB')
btnsale = KeyboardButton('Скидка для WB')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnprice, btnreviews, btnsale)

# ---Menu sale---
btn20 = KeyboardButton('20 процентов')
btn30 = KeyboardButton('30 процентов')
btn40 = KeyboardButton('40 процентов')
btn50 = KeyboardButton('50 процентов')
btnsales = KeyboardButton('Свой % скидки')
btnsalesitem = KeyboardButton('Скидка на товар')
saleMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn20, btn30, btn40, btn50, btnsales, btnsalesitem, main)

# --- Menu Price --- 
btnPriceAll = KeyboardButton('Изменения в ценах')
evrifung = KeyboardButton('🅿️ Поставки')
mainPrice = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPriceAll, evrifung, main)

# --- Menu Deliveries ---
btnOZON = KeyboardButton('Поставки на OZON')
btnWB = KeyboardButton('Поставки на WB')
btnYM = KeyboardButton('Поставки на Яндекс')
btnBackDeliv = KeyboardButton('🔙 Назад к разделам')
mainDeliveries = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOZON, btnWB, btnYM, main, btnBackDeliv)

# --- Menu Deliveries OZON ---
btnOZON_1week = KeyboardButton('OZON поставки на 2 недели')
btnOZON_2week = KeyboardButton('OZON поставки на 4 недели')
btnOZON_3week = KeyboardButton('OZON поставки на 6 недели')
btnOZON_3month = KeyboardButton('OZON поставки на 2 месяца')
mainDelivOZON = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOZON_1week, btnOZON_2week, btnOZON_3week, btnOZON_3month, main, btnBackMarcet)

# --- Menu Deliveries WB ---
btnWB_1week = KeyboardButton('WB поставки на 2 недели')
btnWB_2week = KeyboardButton('WB поставки на 4 недели')
btnWB_3week = KeyboardButton('WB поставки на 6 недели')
btnWB_3month = KeyboardButton('WB поставки на 2 месяца')
mainDelivWB = ReplyKeyboardMarkup(resize_keyboard=True).add(btnWB_1week, btnWB_2week, btnWB_3week, btnWB_3month, main, btnBackMarcet)

# --- Menu Deliveries YM ---
btnYM_1week = KeyboardButton('Яндекс поставки на 2 недели')
btnYM_2week = KeyboardButton('Яндекс поставки на 4 недели')
btnYM_3week = KeyboardButton('Яндекс поставки на 6 недели')
btnYM_3month = KeyboardButton('Яндекс поставки на 2 месяца')
mainDelivYM = ReplyKeyboardMarkup(resize_keyboard=True).add(btnYM_1week, btnYM_2week, btnYM_3week, btnYM_3month, main, btnBackMarcet)