import requests
from bs4 import BeautifulSoup
from time import sleep
url = "https://tygiahomnay.com/ngan-hang-sacombank" #https://oto360.net/dai-ly-mazda/quang-nam.html
response = requests.get(url)
sleep(0.6)
soup=BeautifulSoup(response.content,"html.parser")
tables = soup.find('table', class_='table table-bordered table-hover table-rate')
result = {}
# Lặp qua từng hàng trong bảng
for row in tables.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) > 0:
        # Trích xuất các giá trị cần thiết
        currency_name = cells[0].text.strip()
        buy_rate = float(cells[3].text.strip().split()[0].replace(',', ''))
        sell_rate = float((cells[4].text.strip().split()[0]).replace(',', ''))
        result[currency_name] = {"Mua vào": buy_rate, "Bán ra": sell_rate}


def checkMoneyRate(moneyCategory):
    send = ''
    if(moneyCategory in ("TIỀN ÚC","ĐÔ LA ÚC","ĐÔ ÚC","ĐỒNG ÚC","ĐỒNG AUSTRALIA","TIỀN AUSTRALIA","TỶ GIÁ ĐÔ LA ÚC")):
        keyMoney="Đô la Úc"
    elif (moneyCategory in ("TIỀN CANADA", "ĐÔ LA CANADA", "ĐÔ CANADA", "ĐỒNG ĐÔ LA CANADA", "ĐỒNG CANADA", "TIỀN CANADA", "TỶ GIÁ ĐÔ LA CANADA")):
        keyMoney = "Đô la Canada"
    elif (moneyCategory in ("TIỀN FRANC THỤY SĨ", "ĐÔ LA THỤY SĨ", "ĐÔ THỤY SĨ", "ĐỒNG FRANC", "ĐỒNG FRANC", "TIỀN THỤY SĨ","THỤY SỸ","THỤY SĨ","ĐỒNG THỤY SĨ"
                            "TIỀN FRANC THỤY SỸ", "ĐÔ LA THỤY SỸ", "ĐÔ THỤY SỸ", "ĐỒNG FRANC THỤY SỸ", "TIỀN THỤY SỸ","ĐỒNG THỤY SỸ","FRANC THỤY SĨ","FRANC THỤY SỸ")):
        keyMoney = "Franc Thuỵ Sĩ"

    elif (moneyCategory in ("TỶ GIÁ NHÂN DÂN TỆ","NHÂN DÂN TỆ", "TỆ", "TIỀN NHÂN DÂN TỆ", "ĐỒNG NHÂN DÂN TỆ", "TIỀN TRUNG QUỐC", "TIỀN TRUNG HOA")):
        keyMoney = "Nhân Dân Tệ"

    elif (moneyCategory in ("TIỀN KRONE", "KRONE", "TIỀN ĐAN MẠCH", "ĐỒNG KRONE", "ĐỒNG KRONE ĐAN MẠCH", "TIỀN ĐAN MẠCH","ĐAN MẠCH")):
        keyMoney = "Krone Đan Mạch"

    elif (moneyCategory in ("TIỀN HỒNG KÔNG", "ĐÔ LA HỒNG CÔNG","ĐÔ LA HỒNG KÔNG", "ĐÔ ÚC", "ĐỒNG HỒNG KÔNG", "ĐỒNG ĐÔ LA HỒNG KÔNG", "TIỀN HỒNG KÔNG","HỒNG KÔNG")):
        keyMoney = "Đô la Hồng Kông"

    elif (moneyCategory in ("TIỀN YÊN", "YÊN NHẬT", "YÊN", "ĐỒNG YÊN NHẬT", "ĐỒNG YÊN", "YÊN","YÊN","NHẬT","NHẬT BẢN")):
        keyMoney = "Yên Nhật"

    elif (moneyCategory in ("TIỀN CAM", "TIỀN CAMPUCHIA", "RIÊL", "ĐỒNG RIÊL", "ĐỒNG RIÊL CAMPUCHIA", "CAMPUCHIA","RIÊL","CAM","CAMPUCHIA")):
        keyMoney = "Riêl Campuchia"

    elif (moneyCategory in ("TIỀN WON", "WON HÀN QUỐC", "WON", "ĐỒNG WON HÀN", "ĐỒNG WON", "TỶ GIÁ WON","TỈ GIÁ WON","HÀN QUỐC","HÀN")):
        keyMoney = "Won Hàn Quốc"

    elif (moneyCategory in ("TIỀN KIP LÀO", "KIP LÀO","KÍP LÀO", "KÍP","KIP","LÀO", "ĐỒNG KIP LÀO", "ĐỒNG KÍP", "TỶ GIÁ KÍP", "TỈ GIÁ KÍP LÀO", "LÀO", "LAO")):
        keyMoney = "Kip Lào"

    elif (moneyCategory in ("TIỀN RINGIT MALAI", "RINGIT MALAYSIA", "RINGIT","MALAYSIA","MALAI", "ĐỒNG RINGIT MALAYSIA", "ĐỒNG RINGIT", "TỶ GIÁ RINGIT", "TỈ GIÁ RINGIT", "TIỀN MALAI", "MALAISIA")):
        keyMoney = "Ringit Malaysia"

    elif (moneyCategory in ("TIỀN KRONE NA UY", "KRONE NA UY", "TIỀN NA UY", "ĐỒNG KRONE NA UY", "ĐỒNG KRONE NA UY", "TIỀN KRONE NA UY","NA UY","ĐỒNG NA UY")):
        keyMoney = "Krone Na Uy"

    elif (moneyCategory in ("ĐÔ LA NEW ZEALAND", "ĐÔ LA NEWZEALAND", "NEW ZEALAND","NEWZEALAND", "ĐỒNG NEW ZEALAND", "ĐỒNG ĐÔ LA NEWZEALAND", "TỶ GIÁ NEW ZEALAND","TỈ GIÁ NEWZEALAND")):
        keyMoney = "Ðô la New Zealand"

    elif (moneyCategory in ("TIỀN PHILIPPIN","TIỀN PESO", "PESO PHILIPPIN", "PESO", "ĐỒNG PESO", "ĐỒNG PESO PHILIPPIN", "TỶ GIÁ PESO","TỈ GIÁ PESO","PHILIPPIN")):
        keyMoney = "Peso Philippin"

    elif (moneyCategory in ("TIỀN KRONA THỤY ĐIỂN", "KRONA", "THỤY ĐIỂN", "ĐỒNG KRONA", "ĐỒNG THỤY ĐIỂN", "TỶ GIÁ KRONA","TỈ GIÁ KRONA")):
        keyMoney = "Krona Thuỵ Điển"

    elif (moneyCategory in ("TIỀN BẠC THÁI", "TIỀN THÁI LAN", "THÁI LAN", "ĐỒNG BẠC THÁI", "THÁI", "TỶ GIÁ BẠC THÁI","TỈ GIÁ BẠC THÁI","ĐỒNG BẠC","BẠC THÁI",  "TIỀN BẠT THÁI", "TIỀN THÁI LAN", "THÁI LAN", "ĐỒNG BẠT THÁI", "THÁI", "BẠT THÁI","TỈ GIÁ BẠT THÁI","ĐỒNG BẠT","BẠT THÁI")):
        keyMoney = "Bạc Thái"

    elif (moneyCategory in ("TIỀN ĐÔ LA ĐÀI LOAN","TIỀN ĐÀI LOAN", "ĐÔ LA ĐÀI LOAN", "ĐÀI", "ĐỒNG ĐÔ LA ĐÀI LOAN","ĐÀI LOAN", "ĐỒNG ĐÀI LOAN", "TỶ GIÁ ĐÔ LA ĐÀI LOAN","ĐÔ LA ĐÀI LOAN","DOLA ĐÀI LOAN")):
        keyMoney = "Đô la Đài Loan"

    elif (moneyCategory in ("TIỀN ĐÔ LA MỸ", "TIỀN MỸ", "ĐÔ LA MỸ", "MỸ", "ĐỒNG ĐÔ LA MỸ", "ĐỒNG ĐÔ LA", "DOLA MỸ","DOLA MỸ", "USD", "DOLA MĨ",
                            "USA", "TIỀN ĐÔ LA MĨ", "TIỀN MĨ", "ĐÔ LA MĨ", "MĨ", "ĐỒNG ĐÔ LA MĨ", "ĐỒNG ĐÔ LA USA", "TỶ GIÁ ĐÔ LA MĨ","TỈ GIÁ ĐÔ LA MĨ")):
        keyMoney = "Đô la Mỹ"

    else:
        keyMoney = "dont"

    try:
        buy = result[keyMoney]["Mua vào"]
        sell = result[keyMoney]["Bán ra"]
        send = f"Tỷ giá {keyMoney} có giá mua vào là {buy} đồng và có giá bán ra là {sell} đồng"
        return send
    except:
        send = "Chưa cập nhật tỷ giá"
        return send

