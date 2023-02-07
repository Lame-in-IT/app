import time
import psycopg2
import itertools
from config_BD import host, user, password, database, port
from get_date import get_date
import csv

attempt = 0
count = 0
count_OZON = 0
count_WB = 0

def count_1():
    global count
    count += 1

def count_1_OZON():
    global count_OZON
    count_OZON += 1

def count_1_WB():
    global count_WB
    count_WB += 1

def constat():
    global attempt
    attempt += 1

def get_deviations_OZON():
    try:
        date_1 = get_date()
        corrent_date = date_1[0]
        last_day = date_1[1]
        connection = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        connection.autocommit = True
        list_market_OZON = []
        list_day_OZON = []
        list_name_OZON = []
        list_link_OZON = []
        list_old_pric_OZON = []
        list_new_pric_OZON = []
        list_pric_OZON = []
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT EXISTS (SELECT * FROM price_MARKET_OZON WHERE Дата_проверки = '{corrent_date}');"""
            )
            list_curs = cursor.fetchall()
        if list_curs[0][0] == True:
            list_full_pr_OZON = []
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""SELECT * from price_MARKET_OZON WHERE Дата_проверки = '{corrent_date}';"""
                )
                list_Старая_цена = cursor.fetchall()
                for iten_Старая_цена in list_Старая_цена:
                    for item_Старая_цена in range(0, len(iten_Старая_цена), 6):
                        list_full_pr_OZON.append(list(itertools.islice(iten_Старая_цена, item_Старая_цена, item_Старая_цена + 6)))
            for item_OZON in list_full_pr_OZON:
                if item_OZON[3] == 0 and item_OZON[2] > 0:
                    list_market_OZON.append("OZON")
                    list_day_OZON.append(item_OZON[4])
                    list_name_OZON.append(item_OZON[1])
                    list_link_OZON.append(item_OZON[5])
                    list_old_pric_OZON.append(item_OZON[2])
                    list_new_pric_OZON.append(item_OZON[3])
                    list_pric_OZON.append("Закончился на сайте")
                    count_1()
                    count_1_OZON()
                elif item_OZON[3] > 0 and item_OZON[2] == 0:
                    list_market_OZON.append("OZON")
                    list_day_OZON.append(item_OZON[4])
                    list_name_OZON.append(item_OZON[1])
                    list_link_OZON.append(item_OZON[5])
                    list_old_pric_OZON.append(item_OZON[2])
                    list_new_pric_OZON.append(item_OZON[3])
                    list_pric_OZON.append("Появился на сайте")
                    count_1()
                    count_1_OZON()
                elif item_OZON[3] > item_OZON[2]:
                    max_price_OZON = int(item_OZON[3]) - int(item_OZON[2])
                    list_market_OZON.append("OZON")
                    list_day_OZON.append(item_OZON[4])
                    list_name_OZON.append(item_OZON[1])
                    list_link_OZON.append(item_OZON[5])
                    list_old_pric_OZON.append(item_OZON[2])
                    list_new_pric_OZON.append(item_OZON[3])
                    list_pric_OZON.append(f"Цена повысилась на {max_price_OZON} руб.")
                    count_1()
                    count_1_OZON()
                elif item_OZON[3] < item_OZON[2]:
                    min_price_OZON = int(item_OZON[2]) - int(item_OZON[3])
                    list_market_OZON.append("OZON")
                    list_day_OZON.append(item_OZON[4])
                    list_name_OZON.append(item_OZON[1])
                    list_link_OZON.append(item_OZON[5])
                    list_old_pric_OZON.append(item_OZON[2])
                    list_new_pric_OZON.append(item_OZON[3])
                    list_pric_OZON.append(f"Цена снизилась на {min_price_OZON} руб.")
                    count_1()
                    count_1_OZON()
        elif list_curs[0][0] == False:
            list_full_pr_OZON_1 = []
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""SELECT * from price_MARKET_OZON WHERE Дата_проверки = '{last_day}';"""
                )
                list_Старая_цена_1 = cursor.fetchall()
                for iten_Старая_цена_1 in list_Старая_цена_1:
                    for item_Старая_цена_1 in range(0, len(iten_Старая_цена_1), 6):
                        list_full_pr_OZON_1.append(list(itertools.islice(iten_Старая_цена_1, item_Старая_цена_1, item_Старая_цена_1 + 6)))
            for item_OZON_1 in list_full_pr_OZON_1:
                if item_OZON_1[3] == 0 and item_OZON_1[2] > 0:
                    list_market_OZON.append("OZON")
                    list_day_OZON.append(item_OZON_1[4])
                    list_name_OZON.append(item_OZON_1[1])
                    list_link_OZON.append(item_OZON_1[5])
                    list_old_pric_OZON.append(item_OZON[2])
                    list_new_pric_OZON.append(item_OZON[3])
                    list_pric_OZON.append("Закончился на сайте")
                    count_1()
                    count_1_OZON()
                elif item_OZON_1[3] > 0 and item_OZON_1[2] == 0:
                    list_market_OZON.append("OZON")
                    list_day_OZON.append(item_OZON_1[4])
                    list_name_OZON.append(item_OZON_1[1])
                    list_link_OZON.append(item_OZON_1[5])
                    list_old_pric_OZON.append(item_OZON[2])
                    list_new_pric_OZON.append(item_OZON[3])
                    list_pric_OZON.append("Появился на сайте")
                    count_1()
                    count_1_OZON()
                elif item_OZON_1[3] > item_OZON_1[2]:
                    max_price_OZON_1 = int(item_OZON_1[3]) - int(item_OZON_1[2])
                    list_market_OZON.append("OZON")
                    list_day_OZON.append(item_OZON_1[4])
                    list_name_OZON.append(item_OZON_1[1])
                    list_link_OZON.append(item_OZON_1[5])
                    list_old_pric_OZON.append(item_OZON[2])
                    list_new_pric_OZON.append(item_OZON[3])
                    list_pric_OZON.append(f"Цена повысилась на {max_price_OZON_1} руб.")
                    count_1()
                    count_1_OZON()
                elif item_OZON_1[3] < item_OZON_1[2]:
                    min_price_OZON_1 = int(item_OZON_1[2]) - int(item_OZON_1[3])
                    list_market_OZON.append("OZON")
                    list_day_OZON.append(item_OZON_1[4])
                    list_name_OZON.append(item_OZON_1[1])
                    list_link_OZON.append(item_OZON_1[5])
                    list_old_pric_OZON.append(item_OZON[2])
                    list_new_pric_OZON.append(item_OZON[3])
                    list_pric_OZON.append(f"Цена снизилась на {min_price_OZON_1} руб.")
                    count_1()
                    count_1_OZON()
        return [list_market_OZON, list_day_OZON, list_name_OZON, list_link_OZON, list_old_pric_OZON, list_new_pric_OZON, list_pric_OZON]
    except Exception as ex:
        if attempt <= 5:
            time.sleep(30)
            constat()
            get_deviations_OZON()
    finally:
        if connection:
            connection.close()

def get_deviations_WB():
    try:
        date_1 = get_date()
        corrent_date = date_1[0]
        last_day = date_1[1]
        connection = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        connection.autocommit = True
        list_market_WB = []
        list_day_WB = []
        list_name_WB = []
        list_link_WB = []
        list_old_pric_WB = []
        list_new_pric_WB = []
        list_pric_WB = []
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT EXISTS (SELECT * FROM price_MARKET_WB WHERE Дата_проверки = '{corrent_date}');"""
            )
            list_curs = cursor.fetchall()
        if list_curs[0][0] == True:
            list_full_pr_WB = []
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""SELECT * from price_MARKET_WB WHERE Дата_проверки = '{corrent_date}';"""
                )
                list_Старая_цена = cursor.fetchall()
                for iten_Старая_цена in list_Старая_цена:
                    for item_Старая_цена in range(0, len(iten_Старая_цена), 6):
                        list_full_pr_WB.append(list(itertools.islice(iten_Старая_цена, item_Старая_цена, item_Старая_цена + 6)))
            for item_WB in list_full_pr_WB:
                if item_WB[3] == 0 and item_WB[2] > 0:
                    list_market_WB.append("WB")
                    list_day_WB.append(item_WB[4])
                    list_name_WB.append(item_WB[1])
                    list_link_WB.append(item_WB[5])
                    list_old_pric_WB.append(item_WB[2])
                    list_new_pric_WB.append(item_WB[3])
                    list_pric_WB.append("Закончился на сайте")
                    count_1()
                    count_1_WB()
                elif item_WB[3] > 0 and item_WB[2] == 0:
                    list_market_WB.append("WB")
                    list_day_WB.append(item_WB[4])
                    list_name_WB.append(item_WB[1])
                    list_link_WB.append(item_WB[5])
                    list_old_pric_WB.append(item_WB[2])
                    list_new_pric_WB.append(item_WB[3])
                    list_pric_WB.append("Появился на сайте")
                    count_1()
                    count_1_WB()
                elif item_WB[3] > item_WB[2]:
                    max_price_WB = int(item_WB[3]) - int(item_WB[2])
                    list_market_WB.append("WB")
                    list_day_WB.append(item_WB[4])
                    list_name_WB.append(item_WB[1])
                    list_link_WB.append(item_WB[5])
                    list_old_pric_WB.append(item_WB[2])
                    list_new_pric_WB.append(item_WB[3])
                    list_pric_WB.append(f"Цена повысилась на {max_price_WB} руб.")
                    count_1()
                    count_1_WB()
                elif item_WB[3] < item_WB[2]:
                    min_price_WB = int(item_WB[2]) - int(item_WB[3])
                    list_market_WB.append("WB")
                    list_day_WB.append(item_WB[4])
                    list_name_WB.append(item_WB[1])
                    list_link_WB.append(item_WB[5])
                    list_old_pric_WB.append(item_WB[2])
                    list_new_pric_WB.append(item_WB[3])
                    list_pric_WB.append(f"Цена снизилась на {min_price_WB} руб.")
                    count_1()
                    count_1_WB()
        elif list_curs[0][0] == False:
            list_full_pr_WB_1 = []
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""SELECT * from price_MARKET_WB WHERE Дата_проверки = '{last_day}';"""
                )
                list_Старая_цена_1 = cursor.fetchall()
                for iten_Старая_цена_1 in list_Старая_цена_1:
                    for item_Старая_цена_1 in range(0, len(iten_Старая_цена_1), 6):
                        list_full_pr_WB_1.append(list(itertools.islice(iten_Старая_цена_1, item_Старая_цена_1, item_Старая_цена_1 + 6)))
            for item_WB_1 in list_full_pr_WB_1:
                if item_WB_1[3] == 0 and item_WB_1[2] > 0:
                    list_market_WB.append("WB")
                    list_day_WB.append(item_WB_1[4])
                    list_name_WB.append(item_WB_1[1])
                    list_link_WB.append(item_WB_1[5])
                    list_old_pric_WB.append(item_WB[2])
                    list_new_pric_WB.append(item_WB[3])
                    list_pric_WB.append("Закончился на сайте")
                    count_1()
                    count_1_WB()
                elif item_WB_1[3] > 0 and item_WB_1[2] == 0:
                    list_market_WB.append("WB")
                    list_day_WB.append(item_WB_1[4])
                    list_name_WB.append(item_WB_1[1])
                    list_link_WB.append(item_WB_1[5])
                    list_old_pric_WB.append(item_WB[2])
                    list_new_pric_WB.append(item_WB[3])
                    list_pric_WB.append("Появился на сайте")
                    count_1()
                    count_1_WB()
                elif item_WB_1[3] > item_WB_1[2]:
                    max_price_WB_1 = int(item_WB_1[3]) - int(item_WB_1[2])
                    list_market_WB.append("WB")
                    list_day_WB.append(item_WB_1[4])
                    list_name_WB.append(item_WB_1[1])
                    list_link_WB.append(item_WB_1[5])
                    list_old_pric_WB.append(item_WB[2])
                    list_new_pric_WB.append(item_WB[3])
                    list_pric_WB.append(f"Цена повысилась на {max_price_WB_1} руб.")
                    count_1()
                    count_1_WB()
                elif item_WB_1[3] < item_WB_1[2]:
                    min_price_WB_1 = int(item_WB_1[2]) - int(item_WB_1[3])
                    list_market_WB.append("WB")
                    list_day_WB.append(item_WB_1[4])
                    list_name_WB.append(item_WB_1[1])
                    list_link_WB.append(item_WB_1[5])
                    list_old_pric_WB.append(item_WB[2])
                    list_new_pric_WB.append(item_WB[3])
                    list_pric_WB.append(f"Цена снизилась на {min_price_WB_1} руб.")
                    count_1()
                    count_1_WB()
        return [list_market_WB, list_day_WB, list_name_WB, list_link_WB, list_old_pric_WB, list_new_pric_WB, list_pric_WB]
    except Exception as ex:
        if attempt <= 5:
            time.sleep(30)
            constat()
            get_deviations_WB()
    finally:
        if connection:
            connection.close()

def created_file():
    try:
        date_1 = get_date()
        data_OZON = get_deviations_OZON()
        data_WB = get_deviations_WB()
        if count > 0:
            with open(f'Изменения цен на {date_1[0]}.csv', 'w', encoding='utf_8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        'Маркетплейс',
                        'Дата цен',
                        'Название товара',
                        'Ссылка на товар',
                        'Старая Цена',
                        'Новая Цена',
                        'Изменения в цене',
                    )
                )
            if count_OZON > 0:
                for index_data_OZON, item_data_OZON in enumerate(data_OZON[0]):
                    with open(f'Изменения цен на {date_1[0]}.csv', 'a', encoding='utf_8', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(
                            (
                                item_data_OZON,
                                data_OZON[1][index_data_OZON],
                                data_OZON[2][index_data_OZON],
                                data_OZON[3][index_data_OZON],
                                data_OZON[4][index_data_OZON],
                                data_OZON[5][index_data_OZON],
                                data_OZON[6][index_data_OZON],
                            )
                        )
            if count_WB > 0:
                for index_data_WB, item_data_WB in enumerate(data_WB[0]):
                    with open(f'Изменения цен на {date_1[0]}.csv', 'a', encoding='utf_8', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(
                            (
                                item_data_WB,
                                data_WB[1][index_data_WB],
                                data_WB[2][index_data_WB],
                                data_WB[3][index_data_WB],
                                data_WB[4][index_data_WB],
                                data_WB[5][index_data_WB],
                                data_WB[6][index_data_WB],
                            )
                        )
        return f'Изменения цен на {date_1[0]}.csv'
    except Exception as ex:
        if attempt <= 5:
            time.sleep(30)
            constat()
            created_file()

if __name__ == '__main__':
    created_file()