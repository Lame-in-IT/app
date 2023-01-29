import requests
import schedule
import openpyxl

from headers_OZON import headers_OZON

def raed_xlsx():
    try:
        book_sale = openpyxl.open("sales.xlsx", read_only=True)
        sheet_sale = book_sale.active
        value_sale = sheet_sale["A1"].value
        return value_sale
    except Exception as ex:
        print(ex)

def get_history_price_WB_base():
    try:
        list_article = []
        list_discount = []
        rinquiry = requests.get(
            url='https://suppliers-api.wildberries.ru/public/api/v1/info?quantity=2', headers=headers_OZON).json()
        for item in rinquiry:
            list_article.append(item["nmId"])
            list_discount.append(item["discount"])
        return list_article, list_discount
    except Exception as e:
        print(e)

def discount_WB_minus():
    proch_sale = raed_xlsx()
    data = get_history_price_WB_base()
    list_article = data[0]
    list_discount = data[1]
    try:
        body_1 = []
        for index_1, item_1 in enumerate(list_article):
            if list_discount[index_1] + int(proch_sale) >= 3 and list_discount[index_1] + int(proch_sale) <= 95:
                body_1.append({"discount": list_discount[index_1] + 20, "nm": item_1,})
        rinquiry_1 = requests.post(
                url=f'https://suppliers-api.wildberries.ru/public/api/v1/updateDiscounts', json=body_1, headers=headers_OZON).text
        print(rinquiry_1)
    except Exception as e:
        print(e)
        
def discount_WB():
    proch_sale = raed_xlsx()
    data = get_history_price_WB_base()
    list_article = data[0]
    list_discount = data[1]
    try:
        body_1 = []
        for index_1, item_1 in enumerate(list_article):
            if list_discount[index_1] - int(proch_sale) >= 3 and list_discount[index_1] - int(proch_sale) <= 95:
                body_1.append({"discount": list_discount[index_1] - 20, "nm": item_1,})
        rinquiry_1 = requests.post(
                url=f'https://suppliers-api.wildberries.ru/public/api/v1/updateDiscounts', json=body_1, headers=headers_OZON).text
        print(rinquiry_1)
    except Exception as e:
        print(e)

def main():
    schedule.every().day.at("06:00").do(discount_WB_minus)
    schedule.every().day.at("23:00").do(discount_WB)
    while True:
        schedule.run_pending()

if __name__ == '__main__':
    raed_xlsx()