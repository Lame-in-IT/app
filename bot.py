from tokin_bot import TOKIN
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import asyncio
import aioschedule
from get_reviews_WB import get_reviews_WB
from get_deviations import created_file
from get_Deliveries_OZON import created_file_OZON_1, created_file_OZON_2, created_file_OZON_3, created_file_OZON_4
from get_Deliveries_WB import created_file_WB_1, created_file_WB_2, created_file_WB_3, created_file_WB_4
from get_Deliveries_YM import created_file_YM_1, created_file_YM_2, created_file_YM_3, created_file_YM_4
from min_max_price import created_file_price_min_max
from aiofiles import os
from db import Database

bot = Bot(token=TOKIN, parse_mode="HTML")
dp = Dispatcher(bot)
db = Database('db_WB_OZON.db')

@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Приветствую вас: {0.first_name}'.format(message.from_user), reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message): 
    if message.text == '🪆 Главное меню':
        await bot.send_message(message.from_user.id, '🪆 Главное меню', reply_markup=nav.mainMenu)

    elif message.text == '🅿️ Данные Маркетплейсов':
        await bot.send_message(message.from_user.id, '🅿️ Данные Маркетплейсов', reply_markup=nav.mainPrice)
    
    elif message.text == 'Изменения в ценах':
        await bot.send_message(message.from_user.id, 'Ждите. Идет сбор данных по ценам с площадок...')
        try:
            chat_id = message.chat.id
            await bot_pric(chat_id=chat_id)
        except Exception as e:
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
            await message.answer(e)    

    elif message.text == '📯 Отзывы на WB':
        await bot.send_message(message.from_user.id, 'Введите артикул вместе с Артикул: ')
    
    elif message.text == '🅿️ Поставки':
        await bot.send_message(message.from_user.id, '🅿️ Поставки', reply_markup=nav.mainDeliveries)

    elif message.text == 'Поставки на OZON':
        await bot.send_message(message.from_user.id, 'Поставки на OZON', reply_markup=nav.mainDelivOZON)
    
    elif message.text == 'OZON поставки на 2 недели':
        await bot.send_message(message.from_user.id, 'Ждите. Идет сбор данных по поставкам для OZON...')
        try:
            chat_id = message.chat.id
            await bot_OZON_1(chat_id=chat_id)
        except Exception as e:
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
            await message.answer(e)
        
    elif message.text == 'OZON поставки на 4 недели':
        await bot.send_message(message.from_user.id, 'Ждите. Идет сбор данных по поставкам для OZON...')
        try:
            chat_id = message.chat.id
            await bot_OZON_2(chat_id=chat_id)
        except Exception as e:
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
            await message.answer(e)

    elif message.text == 'OZON поставки на 6 недели':
        await bot.send_message(message.from_user.id, 'Ждите. Идет сбор данных по поставкам для OZON...')
        try:
            chat_id = message.chat.id
            await bot_OZON_3(chat_id=chat_id)
        except Exception as e:
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
            await message.answer(e)

    elif message.text == 'OZON поставки на 2 месяца':
        await bot.send_message(message.from_user.id, 'Ждите. Идет сбор данных по поставкам для OZON...')
        try:
            chat_id = message.chat.id
            await bot_OZON_4(chat_id=chat_id)
        except Exception as e:
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
            await message.answer(e)

    elif message.text == 'WB поставки на 2 недели':
        await bot.send_message(message.from_user.id, 'Ждите. Идет сбор данных по поставкам для OZON...')
        try:
            chat_id = message.chat.id
            await bot_WB_1(chat_id=chat_id)
        except Exception as e:
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
            await message.answer(e)
        
    elif message.text == 'WB поставки на 4 недели':
        await bot.send_message(message.from_user.id, 'Ждите. Идет сбор данных по поставкам для OZON...')
        try:
            chat_id = message.chat.id
            await bot_WB_2(chat_id=chat_id)
        except Exception as e:
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
            await message.answer(e)

    elif message.text == 'WB поставки на 6 недели':
        await bot.send_message(message.from_user.id, 'Ждите. Идет сбор данных по поставкам для OZON...')
        try:
            chat_id = message.chat.id
            await bot_WB_3(chat_id=chat_id)
        except Exception as e:
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
            await message.answer(e)

    elif message.text == 'WB поставки на 2 месяца':
        await bot.send_message(message.from_user.id, 'Ждите. Идет сбор данных по поставкам для OZON...')
        try:
            chat_id = message.chat.id
            await bot_WB_4(chat_id=chat_id)
        except Exception as e:
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
            await message.answer(e)

    elif message.text == 'Яндекс поставки на 2 недели':
        await bot.send_message(message.from_user.id, 'Ждите. Идет сбор данных по поставкам для OZON...')
        try:
            chat_id = message.chat.id
            await bot_YM_1(chat_id=chat_id)
        except Exception as e:
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
            await message.answer(e)
        
    elif message.text == 'Яндекс поставки на 4 недели':
        await bot.send_message(message.from_user.id, 'Ждите. Идет сбор данных по поставкам для OZON...')
        try:
            chat_id = message.chat.id
            await bot_YM_2(chat_id=chat_id)
        except Exception as e:
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
            await message.answer(e)

    elif message.text == 'Яндекс поставки на 6 недели':
        await bot.send_message(message.from_user.id, 'Ждите. Идет сбор данных по поставкам для OZON...')
        try:
            chat_id = message.chat.id
            await bot_YM_3(chat_id=chat_id)
        except Exception as e:
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
            await message.answer(e)

    elif message.text == 'Яндекс поставки на 2 месяца':
        await bot.send_message(message.from_user.id, 'Ждите. Идет сбор данных по поставкам для OZON...')
        try:
            chat_id = message.chat.id
            await bot_YM_4(chat_id=chat_id)
        except Exception as e:
            await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
            await message.answer(e)

    elif message.text == 'Поставки на WB':
        await bot.send_message(message.from_user.id, 'Поставки на WB', reply_markup=nav.mainDelivWB)

    elif message.text == 'Поставки на Яндекс':
        await bot.send_message(message.from_user.id, 'Поставки на Яндекс', reply_markup=nav.mainDelivYM)
    
    elif message.text == '🔙 Назад к разделам':
        await bot.send_message(message.from_user.id, '🔙 Назад к разделам', reply_markup=nav.mainPrice)
    
    elif message.text == '🔙 Маркетплейсы':
        await bot.send_message(message.from_user.id, '🔙 Маркетплейсы', reply_markup=nav.mainDeliveries)
    
    elif (message.text).split(": ")[0] == 'Артикул':
        try:
            await message.answer("Ждите. Идет сбор данных ...")
            chat_id = message.chat.id
            text = (message.text).split(": ")[1]  
            await bot_sta(article=text, chat_id=chat_id)
        except Exception as ex:
            await message.answer("Возникла ошибка. Попробуйте ввести другой артикул.")
    
    elif message.text == 'price':
        if message.chat.type == 'private':
            if message.from_user.id == 1323522063:
                users = db.get_users()
                for item in users:
                    try:
                        files_min_price = created_file_price_min_max()
                        await bot.send_document(chat_id=item[1], document=open(files_min_price, 'rb'))
                        await os.remove(files_min_price)
                        if int(item[2]) != 1:
                            db.set_active(item[1], 1)
                    except Exception as e:
                        db.set_active(item[1], 0)
                        await message.answer("Возникла ошибка. Попробуйте еще раз сделать запрос.")
                    await bot.send_message(message.from_user.id, "Успешная рассылка")
    
    else:
        await message.answer("Возникла ошибка. Введена неизвестная команда.")

async def bot_sta(article, chat_id = ''):
    artic = int(article)
    files_WB = get_reviews_WB(artic)
    file_1 = files_WB[0]
    file_2 = files_WB[1]
    await bot.send_document(chat_id=chat_id, document=open(file_1, 'rb'))
    await bot.send_document(chat_id=chat_id, document=open(file_2, 'rb'))
    await os.remove(file_1)
    await os.remove(file_2)

async def bot_pric(chat_id = ''):
    files_mark = created_file()
    await bot.send_document(chat_id=chat_id, document=open(files_mark, 'rb'))
    await os.remove(files_mark)

async def bot_OZON_1(chat_id = ''):
    files_OZON_1 = created_file_OZON_1()
    await bot.send_document(chat_id=chat_id, document=open(files_OZON_1, 'rb'))
    await os.remove(files_OZON_1)

async def bot_OZON_2(chat_id = ''):
    files_OZON_2 = created_file_OZON_2()
    await bot.send_document(chat_id=chat_id, document=open(files_OZON_2, 'rb'))
    await os.remove(files_OZON_2)

async def bot_OZON_3(chat_id = ''):
    files_OZON_3 = created_file_OZON_3()
    await bot.send_document(chat_id=chat_id, document=open(files_OZON_3, 'rb'))
    await os.remove(files_OZON_3)

async def bot_OZON_4(chat_id = ''):
    files_OZON_4 = created_file_OZON_4()
    await bot.send_document(chat_id=chat_id, document=open(files_OZON_4, 'rb'))
    await os.remove(files_OZON_4)

async def bot_WB_1(chat_id = ''):
    files_WB_1 = created_file_WB_1()
    await bot.send_document(chat_id=chat_id, document=open(files_WB_1, 'rb'))
    await os.remove(files_WB_1)

async def bot_WB_2(chat_id = ''):
    files_WB_2 = created_file_WB_2()
    await bot.send_document(chat_id=chat_id, document=open(files_WB_2, 'rb'))
    await os.remove(files_WB_2)

async def bot_WB_3(chat_id = ''):
    files_WB_3 = created_file_WB_3()
    await bot.send_document(chat_id=chat_id, document=open(files_WB_3, 'rb'))
    await os.remove(files_WB_3)

async def bot_WB_4(chat_id = ''):
    files_WB_4 = created_file_WB_4()
    await bot.send_document(chat_id=chat_id, document=open(files_WB_4, 'rb'))
    await os.remove(files_WB_4)

async def bot_YM_1(chat_id = ''):
    files_YM_1 = created_file_YM_1()
    await bot.send_document(chat_id=chat_id, document=open(files_YM_1, 'rb'))
    await os.remove(files_YM_1)

async def bot_YM_2(chat_id = ''):
    files_YM_2 = created_file_YM_2()
    await bot.send_document(chat_id=chat_id, document=open(files_YM_2, 'rb'))
    await os.remove(files_YM_2)

async def bot_YM_3(chat_id = ''):
    files_YM_3 = created_file_YM_3()
    await bot.send_document(chat_id=chat_id, document=open(files_YM_3, 'rb'))
    await os.remove(files_YM_3)

async def bot_YM_4(chat_id = ''):
    files_YM_4 = created_file_YM_4()
    await bot.send_document(chat_id=chat_id, document=open(files_YM_4, 'rb'))
    await os.remove(files_YM_4)

async def bot_min_price(chat_id = ''):
    files_min_price = created_file_price_min_max()
    await bot.send_document(chat_id=chat_id, document=open(files_min_price, 'rb'))
    await os.remove(files_min_price)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)