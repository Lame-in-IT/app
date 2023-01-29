import requests

from sale.headers_OZON import headers_OZON

def discount_WB_nmId(nmId, discount):
    try:
        body_1 = [{"discount": int(discount), "nm": int(nmId),}]
        rinquiry_1 = requests.post(
                url=f'https://suppliers-api.wildberries.ru/public/api/v1/updateDiscounts', json=body_1, headers=headers_OZON).text
    except Exception as e:
        print(e)