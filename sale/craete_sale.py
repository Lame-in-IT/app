import openpyxl

def craete_sale(sale):
    try:
        book_sale = openpyxl.Workbook()
        sheet_sale = book_sale.active
        sheet_sale['A1'] = f"{sale}"
        book_sale.save("sale\\sales.xlsx")
        book_sale.close()
    except Exception as ex:
        print(ex)
        
if __name__ == '__main__':
    craete_sale(30)