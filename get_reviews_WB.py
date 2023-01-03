import requests
from fake_useragent import UserAgent
import csv



def get_number_product(imt_id):
    """получение и отправление imtid для товара"""
    a = imt_id
    url = f'https://wbx-content-v2.wbstatic.net/ru/{a}.json'
    response = requests.get(url=url).json()
    return response["imt_id"], response["nm_id"]


def get_reviews_WB(nm_id):
    """получение отзывов и запись всех записей и повторяющихся в файл .csv """    
    imtid = get_number_product(nm_id)[0]
    nmid = get_number_product(nm_id)[1]
    ua = UserAgent()    
    client_ua = ua.random
    with open(f'Все отзывы {nmid}.csv', 'w', encoding='utf_8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Ник автора',
                'Текст отзыва',
                'Оценка товара',
            )
        )
    with open(f'Повторяющиеся отзывы {nmid}.csv', 'w', encoding='utf_8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Текст отзыва',
                'Количество повторений',
                'Оценка товара',
            )
        )
    count = 0
    count_page = 1
    count_feedbacks = 30
    list_text = []
    list_slov = []
    list_povtor_slov = []
    list_number_com = []
    list_ochenka = []
    while count_feedbacks == 30:
        headers ={
            'User-Agent': client_ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Content-Type': 'application/json'
        }    
        body = {
            "imtId": imtid,
            "skip": count,
            "take": 30
        } 
        url_WB = "https://public-feedbacks.wildberries.ru/api/v1/summary/full"
        response = requests.post(url=url_WB, json=body , headers=headers).json()       
        for item in response["feedbacks"]:            
            name_client = item["wbUserDetails"]["name"]
            text = item["text"]
            ochenc = item["productValuation"]
            text_client = item["text"].replace('!', ',').replace('?', ',').replace('.', ',').replace(';', ',').replace(':', ',').replace(')', ',').replace('(', ',')
            text_razdel = text_client.split(',') 
            with open(f'Все отзывы {nmid}.csv', 'a', encoding='utf_8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        name_client,
                        text,
                        ochenc,
                    )
                )          
            for item_slova in text_razdel:
                if item_slova not in list_slov:
                    list_slov.append(item_slova.strip())
                elif item_slova in list_slov:
                    if item_slova not in " " and item_slova not in "":
                        if item_slova not in list_povtor_slov:
                            list_povtor_slov.append(item_slova.strip())
                            list_number_com.append(1)
                            list_ochenka.append(item["productValuation"])
                        for ind, ite in enumerate(list_povtor_slov):
                            if item_slova in ite:
                                list_number_com[ind] += 1         
        feedbacks = len(response["feedbacks"])
        if feedbacks == 30:
            count = count + 30
            count_page = count_page + 1
        elif feedbacks < 30:
            break
    for index_csv, item_csv in enumerate(list_povtor_slov):
        with open(f'Повторяющиеся отзывы {nmid}.csv', 'a', encoding='utf_8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    item_csv,
                    list_number_com[index_csv],
                    list_ochenka[index_csv],
                )
            )
    return f'Все отзывы {nmid}.csv', f'Повторяющиеся отзывы {nmid}.csv'


if __name__ == '__main__':
    get_reviews_WB()