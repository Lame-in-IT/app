import time
import psycopg2
import itertools
import openpyxl
from dict_min_max_price import dict_min_max_price
from config_BD import host, user, password, database, port
from get_date import get_date

attempt = 0
count = 0

def constat():
    global attempt
    attempt += 1

def count_1():
    global count
    count += 1

def min_max_price():
    try:
        date_1 = get_date()
        corrent_date = date_1[0]
        connection = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        connection.autocommit = True
        list_full_stoc_OZON = []
        list_full_stoc_WB = []
        list_market = []
        list_article = []
        list_name = []
        list_old_price = []
        list_new_price = []
        list_date_price = []
        list_link = []
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT * from price_MARKET_OZON WHERE Дата_проверки = '{corrent_date}';"""
            )
            list_remains = cursor.fetchall()
            for iten_remains in list_remains:
                for item_remains in range(0, len(iten_remains), 6):
                    list_full_stoc_OZON.append(list(itertools.islice(iten_remains, item_remains, item_remains + 6)))
        for item_OZON in list_full_stoc_OZON:
            list_market.append("OZON")
            list_article.append(item_OZON[0])
            list_name.append(item_OZON[1])
            list_old_price.append(item_OZON[2])
            list_new_price.append(item_OZON[3])
            list_date_price.append(item_OZON[4])
            list_link.append(item_OZON[5])
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT * from price_MARKET_WB WHERE Дата_проверки = '{corrent_date}';"""
            )
            list_remains_1 = cursor.fetchall()
            for iten_remains_1 in list_remains_1:
                for item_remains_1 in range(0, len(iten_remains_1), 6):
                    list_full_stoc_WB.append(list(itertools.islice(iten_remains_1, item_remains_1, item_remains_1 + 6)))
        for item_WB in list_full_stoc_WB:
            list_market.append("Wildberries")
            list_article.append(item_WB[0])
            list_name.append(item_WB[1])
            list_old_price.append(item_WB[2])
            list_new_price.append(item_WB[3])
            list_date_price.append(item_WB[4])
            list_link.append(item_WB[5])
        return [list_market, list_article, list_name, list_old_price,
                list_new_price, list_date_price, list_link]
    except Exception as ex:
        if attempt <= 5:
            time.sleep(30)
            constat()
            min_max_price()
    finally:
        if connection:
            connection.close()

def midle_price():
    try:
        list_data_price = min_max_price()
        list_market = []
        list_article = []
        list_name = []
        list_new_price = []
        list_pred_price = []
        list_date_price = []
        list_midle = []
        list_link = []
        for index, item in enumerate(list_data_price[0]):
            if list_data_price[4][index] != 0:
                if list_data_price[4][index] > dict_min_max_price[list_data_price[2][index]][0][1]:
                    list_market.append(list_data_price[0][index])
                    list_article.append(list_data_price[1][index])
                    list_name.append(list_data_price[2][index])
                    list_new_price.append(list_data_price[4][index])
                    list_pred_price.append(f"Максимальная цена {dict_min_max_price[list_data_price[2][index]][0][1]}")
                    list_date_price.append(list_data_price[5][index])
                    midle_price = list_data_price[4][index] - dict_min_max_price[list_data_price[2][index]][0][1]
                    list_midle.append(f"Цена выше максимальной на {midle_price}")
                    list_link.append(list_data_price[6][index])
                    count_1()
                elif list_data_price[4][index] < dict_min_max_price[list_data_price[2][index]][0][0]:
                    list_market.append(list_data_price[0][index])
                    list_article.append(list_data_price[1][index])
                    list_name.append(list_data_price[2][index])
                    list_new_price.append(list_data_price[4][index])
                    list_pred_price.append(f"Минимальная цена {dict_min_max_price[list_data_price[2][index]][0][0]}")
                    list_date_price.append(list_data_price[5][index])
                    midle_price = dict_min_max_price[list_data_price[2][index]][0][0] - list_data_price[4][index]
                    list_midle.append(f"Цена меньше минимальной на {midle_price}")
                    list_link.append(list_data_price[6][index])
                    count_1()
        return [list_market, list_article, list_name, list_new_price, list_pred_price, list_midle, list_date_price, list_link]
    except Exception as ex:
        print(ex)


def created_file_price_min_max():
    try:
        full_list = midle_price()
        date_now = get_date()
        corrent_date = date_now[0]
        if int(count) > 0:
            book = openpyxl.Workbook()
            sheet = book.active
            sheet["A1"] = "Макетплейс"
            sheet["B1"] = "Артикул товара"
            sheet["C1"] = "Наименование товара"
            sheet["D1"] = "Новая цена"
            sheet["E1"] = "Предельная цена"
            sheet["F1"] = "Разница в цене"
            sheet["G1"] = "Дата проверки"
            sheet["H1"] = "Ссылка на товар"
            for index, item in enumerate(full_list[0]):
                index_sheet = index + 2
                sheet[f"A{index_sheet}"] = item
                sheet[f"B{index_sheet}"] = full_list[1][index]
                sheet[f"C{index_sheet}"] = full_list[2][index]
                sheet[f"D{index_sheet}"] = full_list[3][index]
                sheet[f"E{index_sheet}"] = full_list[4][index]
                sheet[f"F{index_sheet}"] = full_list[5][index]
                sheet[f"G{index_sheet}"] = full_list[6][index]
                sheet[f"H{index_sheet}"] = full_list[7][index]
            book.save(f"Отклонение цен от предельных на {corrent_date}.xlsx")
            book.close()
            return f"Отклонение цен от предельных на {corrent_date}.xlsx"
    except Exception as ex:
        if attempt <= 5:
            time.sleep(30)
            constat()
            created_file_price_min_max()

if __name__ == '__main__':
    created_file_price_min_max()