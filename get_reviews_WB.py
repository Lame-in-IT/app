import requests
from fake_useragent import UserAgent
import openpyxl



def get_number_product(imt_id):
    """получение и отправление imtid для товара"""
    a = str(imt_id)
    url = f'https://wbx-content-v2.wbstatic.net/ru/{a}.json'
    response = requests.get(url=url).json()
    return response["imt_id"], response["nm_id"]

def create_xslx(list_povtor_slov, list_number_com, list_ochenka, nmid):
    book = openpyxl.Workbook()
    sheet = book.active
    sheet["A1"] = "Текст отзыва"
    sheet["B1"] = "Количество повторений"
    sheet["C1"] = "Оценка товара"
    for index, item in enumerate(list_povtor_slov):
        index_sheet = index + 2
        sheet[f"A{index_sheet}"] = item
        sheet[f"B{index_sheet}"] = list_number_com[index]
        sheet[f"C{index_sheet}"] = list_ochenka[index]
    book.save(f'Повторяющиеся отзывы {nmid}.xlsx')
    book.close()


def get_reviews_WB(nm_id):
    """получение отзывов и запись всех записей и повторяющихся в файл .csv """    
    date_for_WB = get_number_product(nm_id)
    imtid = date_for_WB[0]
    nmid = date_for_WB[1]
    ua = UserAgent()    
    client_ua = ua.random
    count = 0
    count_page = 1
    count_feedbacks = 30
    book = openpyxl.Workbook()
    sheet = book.active
    sheet["A1"] = "Ник автора"
    sheet["B1"] = "Текст отзыва"
    sheet["C1"] = "Оценка товара"
    list_slov = []
    list_povtor_slov = []
    list_number_com = []
    list_ochenka = []
    list_index = [0]
    while count_feedbacks == 30:
        headers ={
            'User-Agent': client_ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Content-Type': 'application/json'
        }    
        body = {
            "imtId": imtid,
            "skip": count,
            "take": 30
        } 
        url_WB = "https://public-feedbacks.wildberries.ru/api/v1/summary/full"
        response = requests.post(url=url_WB, json=body , headers=headers).json()
        try:
            for index, item in enumerate(response["feedbacks"]):            
                name_client = item["wbUserDetails"]["name"]
                text = item["text"]
                ochenc = item["productValuation"]
                text_client = item["text"].replace('!', ',').replace('?', ',').replace('.', ',').replace(';', ',').replace(':', ',').replace(')', ',').replace('(', ',')
                text_razdel = text_client.split(',') 
                index_sheet = index + count + 2
                list_index[0] = index_sheet
                sheet[f"A{index_sheet}"] = name_client
                sheet[f"B{index_sheet}"] = text
                sheet[f"C{index_sheet}"] = ochenc       
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
        except Exception as e:
            indexx = list_index[0] + 1
            sheet[f"A{indexx}"] = "Больше отзывов собрать невозможно"
            break
    create_xslx(list_povtor_slov, list_number_com, list_ochenka, nmid)
    book.save(f'Все отзывы {nmid}.xlsx')
    book.close()
    return f'Все отзывы {nmid}.xlsx', f'Повторяющиеся отзывы {nmid}.xlsx'

if __name__ == '__main__':
    get_reviews_WB()