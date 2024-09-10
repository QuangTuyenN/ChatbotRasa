from typing import Text, List, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
from download_sql_to_dict_csv import dict_sql
from helpFunction import current_weather, crawl_gold, money_question, today_news
from testCrawlMoney import checkMoneyRate
from positionSqlCsv import dict_position
from công tySubHoldingCsv import dict_company
# from MeetingRoomSql import checkhour

from features_car_csv import dict_feature
from woltframFunction import calculate


class ActionCheckTime(Action):

    def name(self) -> Text:
        return "action_check_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Lấy thời gian hiện tại
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S %Y-%m-%d")

        # Gửi thông điệp về thời gian hiện tại cho người dùng
        dispatcher.utter_message(text=f"Thời gian hiện tại là {current_time}.")
        return []


class ActionGoogleSearch(Action):

    def name(self) -> Text:
        return "action_google_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(tracker.latest_message)
        # Lấy entity đã trích xuất từ câu intent trước đó
        try:
            keyword = tracker.latest_message['entities'][0]['value']
            send = f"Đây là những tính năng mới của xe {keyword}:"
        except:
            send = "Không biết bạn muốn hỏi tính năng xe gì?"

        # Hiển thị kết quả tìm kiếm cho người dùng
        dispatcher.utter_message("{}".format(send))

        return []


class ActionResponseCarBrand(Action):

    def name(self) -> Text:
        return "action_car_brand"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Lấy entity đã trích xuất từ câu intent trước đó
        keyword = tracker.latest_message['entities'][0]['value']
        responsecarbrand = ''
        if (keyword == 'Mercedes') or (keyword == 'Mercedes'):
            responsecarbrand = 'Hiện tại Mercedes có các model xe Mercedes 2, Mercedes 2 Sport, Mercedes 3, Mercedes 3 Sport, Mercedes CX-30, Mercedes CX-3, Mercedes BT-50, Mercedes CX-5, Mercedes CX-8, không biết bạn đang muốn tham khảo giá model nào?'
        elif (keyword == 'Kia') or (keyword == 'kia'):
            responsecarbrand = 'Hiện tại Kia có các model xe Kia Morning, Kia New Morning, Kia Soluto, Kia Sonet, Kia Carens, Kia K3, Kia Seltos, Kia K5, Kia Sportage, Kia Sorento, Kia Carnival, Kia Sorento Hybrid không biết bạn đang muốn tham khảo giá model nào?'
        elif (keyword == 'Peugeot') or (keyword == 'peugeot'):
            responsecarbrand = 'Hiện tại Peugeot có các model xe Peugeot 2008, 3008, 5008, Peugeot Traveller không biết bạn đang muốn tham khảo giá xe model nào?'
        elif (keyword == 'huyndai') or (keyword == 'Huyndai'):
            responsecarbrand = 'Hiện tại Huyndai có các model xe Huyndai 3 Series, X3, 5 Series, 4 Series Grand Coupe, 4 Series Mui Trần, Z4, X4, X5, X6, 7 Series, X7, 8 Series, I7, không biết bạn muốn tham khảo model nào?'
        elif (keyword == 'MINI') or (keyword == 'MINI Cooper') or (keyword == 'mini'):
            responsecarbrand = 'Hiện tại MINI có các model xe MINI Cooper One 5 Door, MINI Cooper 3 Door, MINI Cooper Convertible, MINI Cooper Countryman, MINI Cooper Clubman, không biết bạn muốn tham khảo model nào?'
        # Hiển thị kết quả tìm kiếm cho người dùng
        dispatcher.utter_message(responsecarbrand)

        return []

class ActionResponseFeaturesCarBrand(Action):

    def name(self) -> Text:
        return "action_features_car_brand"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Lấy entity đã trích xuất từ câu intent trước đó
        keyword = tracker.latest_message['entities'][0]['value']
        responsecarbrand = ''
        if (keyword == 'Mercedes') or (keyword == 'Mercedes'):
            responsecarbrand = 'Hiện tại Mercedes có các model xe Mercedes 2, Mercedes 2 Sport, Mercedes 3, Mercedes 3 Sport, Mercedes CX-30, Mercedes CX-3, Mercedes BT-50, Mercedes CX-5, Mercedes CX-8, không biết bạn đang muốn tham khảo tính năng model nào?'
        elif (keyword == 'Kia') or (keyword == 'kia'):
            responsecarbrand = 'Hiện tại Kia có các model xe Kia Morning, Kia New Morning, Kia Soluto, Kia Sonet, Kia Carens, Kia K3, Kia Seltos, Kia K5, Kia Sportage, Kia Sorento, Kia Carnival, Kia Sorento Hybrid không biết bạn đang muốn tham khảo tính năng model nào?'
        elif (keyword == 'Peugeot') or (keyword == 'peugeot'):
            responsecarbrand = 'Hiện tại Peugeot có các model xe Peugeot 2008, 3008, 5008, Peugeot Traveller không biết bạn đang muốn tham khảo tính năng model nào?'
        elif (keyword == 'huyndai') or (keyword == 'Huyndai'):
            responsecarbrand = 'Hiện tại Huyndai có các model xe Huyndai 3 Series, X3, 5 Series, 4 Series Grand Coupe, 4 Series Mui Trần, Z4, X4, X5, X6, 7 Series, X7, 8 Series, I7, không biết bạn muốn tham khảo tính năng model nào?'
        elif (keyword == 'MINI') or (keyword == 'MINI Cooper') or (keyword == 'mini'):
            responsecarbrand = 'Hiện tại MINI có các model xe MINI Cooper One 5 Door, MINI Cooper 3 Door, MINI Cooper Convertible, MINI Cooper Countryman, MINI Cooper Clubman, không biết bạn muốn tham khảo tính năng model nào?'
        # Hiển thị kết quả tìm kiếm cho người dùng
        dispatcher.utter_message(responsecarbrand)

        return []
# class ActionCheckCarPriceFromSql(Action):
#
#     def name(self) -> Text:
#         return "action_car_price"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         price = ""
#         img_url = ''
#         # Lấy entity đã trích xuất từ câu intent trước đó
#         keyword = tracker.latest_message['entities'][0]['value']
#
#         print("keyword ", keyword)
#         try:
#             if ("Mercedes" in keyword) or ("Mercedes" in keyword) or ("Mercedes" in keyword):
#                 if ("cx" in keyword) or ("CX" in keyword) and ("-" not in keyword):
#                     keyword = keyword.title()
#                     keyword = keyword.replace("Cx","CX-")
#                 elif ("cx" in keyword) or ("CX" in keyword) and ("-" in keyword):
#                     keyword = keyword.title()
#                     keyword = keyword.replace("Cx", "CX")
#                 else:
#                     keyword = keyword.title()
#
#                 for key, value in dict_sql["car"]['Mercedes'][keyword].items():
#                     str = f"Xe {key} có giá đề xuất là {value['Suggest_Price']} ; Giá lăn bánh thành phố là {value['Rolling_Price_City']} ; Giá lăn bánh tỉnh là {value['Rolling_Price_Suburban']}"
#                     price = price + ". " + str
#                     img_url = value['Image_URL']
#             elif ("Kia" in keyword) or ("kia" in keyword):
#                 keyword = keyword.title()
#                 for key, value in dict_sql["car"]['Kia'][keyword].items():
#                     str = f"Xe {key} có giá đề xuất là {value['Suggest_Price']} ; Giá lăn bánh thành phố là {value['Rolling_Price_City']} ; Giá lăn bánh tỉnh là {value['Rolling_Price_Suburban']}"
#                     price = price + ". " + str
#                     img_url = value['Image_URL']
#             elif ("Peugeot" in keyword) or ("peugeot" in keyword):
#                 keyword = keyword.title()
#                 for key, value in dict_sql["car"]['Peugeot'][keyword].items():
#                     str = f"Xe {key} có giá đề xuất là {value['Suggest_Price']} ; Giá lăn bánh thành phố là {value['Rolling_Price_City']} ; Giá lăn bánh tỉnh là {value['Rolling_Price_Suburban']}"
#                     price = price + ". " + str
#                     img_url = value['Image_URL']
#             elif ("Huyndai" in keyword) or ("Huyndai" in keyword):
#                 for key, value in dict_sql["car"]['Huyndai'][keyword].items():
#                     str = f"Xe {key} có giá đề xuất là {value['Suggest_Price']} ; Giá lăn bánh thành phố là {value['Rolling_Price_City']} ; Giá lăn bánh tỉnh là {value['Rolling_Price_Suburban']}"
#                     price = price + ". " + str
#                     img_url = value['Image_URL']
#             elif ("MINI" in keyword) or ("mini" in keyword):
#                 for key, value in dict_sql["car"]['MINI Cooper'][keyword].items():
#                     str = f"Xe {key} có giá đề xuất là {value['Suggest_Price']} ; Giá lăn bánh thành phố là {value['Rolling_Price_City']} ; Giá lăn bánh tỉnh là {value['Rolling_Price_Suburban']}"
#                     price = price + ". " + str
#                     img_url = value['Image_URL']
#         except Exception as bug:
#             print("bug: ", bug)
#             price = "Xin lỗi nhưng model bạn lựa chọn dường như không tồn tại, vui lòng ghi đúng model ô tô"
#
#         # Hiển thị kết quả tìm kiếm cho người dùng
#         dispatcher.utter_message("{}".format(price))
#         # Gửi phản hồi kèm hình ảnh
#         dispatcher.utter_message(image=img_url)
#
#         return []


class ActionCheckWeather(Action):

    def name(self) -> Text:
        return "action_check_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Lấy entity đã trích xuất từ câu intent trước đó
        try:
            print(tracker.latest_message)
            keyword = tracker.latest_message['entities'][0]['value']
            if (keyword.upper() == 'THỦ ĐÔ'):
                keyword = 'Hà Nội'
            elif (keyword.upper() == 'SÀI GÒN') or (keyword.upper() == 'HỒ CHÍ MINH'):
                keyword = 'Thành phố Hồ Chí Minh'
            weather = current_weather(keyword)
            keyword = keyword.title()
            if weather == "Xin lỗi":
                weather = f"Xin lỗi nhưng hiện tại tôi chưa có thông tin về thời tiết tại {keyword}"
        except:
            weather = "Vui lòng cho biết địa điểm bạn muốn cập nhật thông tin thời tiết"

        # Hiển thị kết quả tìm kiếm cho người dùng
        dispatcher.utter_message("{}".format(weather))

        return []


class ActionCheckGoldPrice(Action):

    def name(self) -> Text:
        return "action_gold_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print('action giá vàng')
        price = ""
        goldPrice = crawl_gold()
        for key, value in goldPrice.items():
            str = f"Vàng {key} có giá mua vào là {value['Mua vào']} ; Giá bán ra là {value['Bán ra']}"
            price = price + ". " + str

        # Hiển thị kết quả tìm kiếm cho người dùng
        dispatcher.utter_message("{}".format(price))

        return []


class ActionCheckMoneyExchange(Action):

    def name(self) -> Text:
        return "action_money_exchange"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        keyword = tracker.latest_message['entities'][0]['value']
        print(keyword)
        keyword_upper = keyword.upper()
        moneyExchange = checkMoneyRate(keyword_upper)
        # Hiển thị kết quả tìm kiếm cho người dùng
        dispatcher.utter_message(moneyExchange)
        return []


class ActionCheckTodayNews(Action):

    def name(self) -> Text:
        return "action_today_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        news = today_news()

        # Hiển thị kết quả tìm kiếm cho người dùng
        dispatcher.utter_message(f"Hôm nay có các tin nóng: {news}")

        return []


class ActionCheckPositionFromName(Action):

    def name(self) -> Text:
        return "action_answer_position"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        send = ''
        check = []
        keyword = tracker.latest_message['entities'][0]['value']

        keyword_upper = keyword.upper()
        print(keyword_upper)

        for key, value in dict_position.items():
            if keyword_upper in key:
                send = value
                check.append("1")

        if len(check) == 0:
            chucvu = f"Xin lỗi nhưng tôi không có thông tin về {keyword}"
        else:
            chucvu = send
        # Hiển thị kết quả tìm kiếm cho người dùng
        dispatcher.utter_message(f"{chucvu}")

        return []


class ActionCheckCarPriceFromSql(Action):

    def name(self) -> Text:
        return "action_car_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        price = ""
        img_url = ''
        # Lấy entity đã trích xuất từ câu intent trước đó
        keyword = tracker.latest_message['entities'][0]['value']
        print("tracker ", tracker.latest_message)
        keyword_upper = keyword.upper()
        print("keyword ", keyword)
        list_Mercedes = ['GLC200', 'C300', 'C200', 'G63']
        list_kia = ['MORNING', 'SOLUTO', 'SONET', 'SELTOS', 'CARENS', 'SPORTAGE', 'K3', 'K5', 'SORENTO', 'CARNIVAL']
        list_peugeot = ['2008', '3008', '5008', 'TRAVELLER']
        list_Huyndai = ['Acent', 'i10', 'Elantra', 'Kona', 'Tucson', 'Santafe']
        list_mini = ['DOOR', 'CONVERTIBLE', 'COUNTRYMAN', 'CLUBMAN']
        try:
            for i in list_Mercedes:
                if i in keyword_upper:
                    if 'Mercedes' not in keyword_upper:
                        keyword = 'Mercedes ' + keyword
                    else:
                        keyword = keyword
            for i in list_kia:
                if i in keyword_upper:
                    if 'KIA' not in keyword_upper:
                        keyword = 'Kia ' + keyword
                    else:
                        keyword = keyword
            for i in list_peugeot:
                if i in keyword_upper:
                    if 'PEUGEOT' not in keyword_upper:
                        keyword = 'Peugeot ' + keyword
                    else:
                        keyword = keyword
            for i in list_Huyndai:
                if i in keyword_upper:
                    if 'Huyndai' not in keyword_upper:
                        keyword = 'Huyndai ' + keyword
                    else:
                        keyword = keyword
            for i in list_mini:
                if i in keyword_upper:
                    if 'MINI COOPER' not in keyword_upper:
                        keyword = 'MINI Cooper ' + keyword
                    else:
                        keyword = keyword
            if ("Mercedes" in keyword) or ("mercedes" in keyword) or ("mer" in keyword):
                for key, value in dict_sql["car"]['Mercedes'][keyword].items():
                    str = f"Xe {key}:\n + Giá đề xuất: {value['Suggest_Price']}\n + Giá lăn bánh thành phố: {value['Rolling_Price_City']}\n + Giá lăn bánh tỉnh: {value['Rolling_Price_Suburban']}"
                    price = price + "\n" + str
                    img_url = value['Image_URL']
            elif ("Kia" in keyword) or ("kia" in keyword):
                keyword = keyword.title()
                for key, value in dict_sql["car"]['Kia'][keyword].items():
                    str = f"Xe {key}:\n + Giá đề xuất: {value['Suggest_Price']}\n + Giá lăn bánh thành phố: {value['Rolling_Price_City']}\n + Giá lăn bánh tỉnh: {value['Rolling_Price_Suburban']}"
                    price = price + "\n" + str
                    img_url = value['Image_URL']
            elif ("Peugeot" in keyword) or ("peugeot" in keyword):
                keyword = keyword.title()
                for key, value in dict_sql["car"]['Peugeot'][keyword].items():
                    str = f"Xe {key}\n + Giá đề xuất là {value['Suggest_Price']}\n + Giá lăn bánh thành phố: {value['Rolling_Price_City']}\n + Giá lăn bánh tỉnh: {value['Rolling_Price_Suburban']}"
                    price = price + "\n" + str
                    img_url = value['Image_URL']
            elif ("Huyndai" in keyword) or ("huyndai" in keyword):
                for key, value in dict_sql["car"]['Huyndai'][keyword].items():
                    str = f"Xe {key}\n + Giá đề xuất là {value['Suggest_Price']}\n + Giá lăn bánh thành phố: {value['Rolling_Price_City']}\n + Giá lăn bánh tỉnh: {value['Rolling_Price_Suburban']}"
                    price = price + "\n" + str
                    img_url = value['Image_URL']
            elif ("MINI" in keyword) or ("mini" in keyword):
                for key, value in dict_sql["car"]['MINI Cooper'][keyword].items():
                    str = f"Xe {key}\n + Giá đề xuất là {value['Suggest_Price']}\n + Giá lăn bánh thành phố: {value['Rolling_Price_City']}\n + Giá lăn bánh tỉnh: {value['Rolling_Price_Suburban']}"
                    price = price + "\n" + str
                    img_url = value['Image_URL']
        except Exception as bug:
            print("bug: ", bug)
            price = "Xin lỗi nhưng model bạn lựa chọn dường như không tồn tại, vui lòng ghi đúng model ô tô"

        # Hiển thị kết quả tìm kiếm cho người dùng
        dispatcher.utter_message("{}".format(price))
        # Gửi phản hồi kèm hình ảnh
        dispatcher.utter_message(image=img_url)

        return []

class ActionCheckCarFeaturesFromSql(Action):

    def name(self) -> Text:
        return "action_car_feature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        features = ""
        # Lấy entity đã trích xuất từ câu intent trước đó
        keyword = tracker.latest_message['entities'][0]['value']
        print("tracker ", tracker.latest_message)
        keyword_upper = keyword.upper()
        print("keyword ", keyword)
        list_Mercedes = ['GLC200', 'C300', 'C200', 'G63']
        list_kia = ['MORNING', 'SOLUTO', 'SONET', 'SELTOS', 'CARENS', 'SPORTAGE', 'K3', 'K5', 'SORENTO', 'CARNIVAL']
        list_peugeot = ['2008', '3008', '5008', 'TRAVELLER']
        list_Huyndai = ['SERIES', 'X3', 'X4', 'X5', 'X6', 'X7', 'Z4']
        list_mini = ['DOOR', 'CONVERTIBLE', 'COUNTRYMAN', 'CLUBMAN']
        try:
            for i in list_Mercedes:
                if i in keyword_upper:
                    if 'Mercedes' not in keyword_upper:
                        keyword = 'Mercedes ' + keyword
                    else:
                        keyword = keyword
            for i in list_kia:
                if i in keyword_upper:
                    if 'KIA' not in keyword_upper:
                        keyword = 'Kia ' + keyword
                    else:
                        keyword = keyword
            for i in list_peugeot:
                if i in keyword_upper:
                    if 'PEUGEOT' not in keyword_upper:
                        keyword = 'Peugeot ' + keyword
                    else:
                        keyword = keyword
            for i in list_Huyndai:
                if i in keyword_upper:
                    if 'Huyndai' not in keyword_upper:
                        keyword = 'Huyndai ' + keyword
                    else:
                        keyword = keyword
            for i in list_mini:
                if i in keyword_upper:
                    if 'MINI COOPER' not in keyword_upper:
                        keyword = 'MINI Cooper ' + keyword
                    else:
                        keyword = keyword
            if ("Mercedes" in keyword) or ("Mercedes" in keyword) or ("Mercedes" in keyword):
                if (("cx" in keyword) or ("CX" in keyword)) and ("-" not in keyword):
                    keyword = keyword.title()
                    keyword = keyword.replace("Cx", "CX-")
                elif ("cx" in keyword) or ("CX" in keyword) and ("-" in keyword):
                    keyword = keyword.title()
                    keyword = keyword.replace("Cx", "CX")
                else:
                    keyword = keyword.title()

                for key, value in dict_feature.items():
                    if keyword in key:
                        features = value
            elif ("Kia" in keyword) or ("kia" in keyword):
                keyword = keyword.title()
                for key, value in dict_feature.items():
                    if (keyword in key) and ('Sorento' in keyword) and ('Hybrid' not in keyword):
                        features = value
                    elif keyword in key:
                        features = value
            elif ("Peugeot" in keyword) or ("peugeot" in keyword):
                keyword = keyword.title()
                for key, value in dict_feature.items():
                    if keyword in key:
                        features = value
            elif ("Huyndai" in keyword) or ("Huyndai" in keyword):
                for key, value in dict_feature.items():
                    if keyword in key:
                        features = value
            elif ("MINI" in keyword) or ("mini" in keyword):
                for key, value in dict_feature.items():
                    if keyword in key:
                        features = value
        except Exception as bug:
            print("bug: ", bug)
            features = "Xin lỗi nhưng model bạn lựa chọn dường như không tồn tại, vui lòng ghi đúng model ô tô"

        # Hiển thị kết quả tìm kiếm cho người dùng
        dispatcher.utter_message("{}".format(features))
        # Gửi phản hồi kèm hình ảnh
        # dispatcher.utter_message(image=img_url)

        return []

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Xin lỗi, tôi không hiểu câu hỏi của bạn, vui lòng hỏi cụ thể hơn hoặc chuyển sang một chủ đề khác!")
        return []

class ActionAskEmployeeID(Action):
    def name(self) -> Text:
        return "action_ask_employee_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_events = [event for event in tracker.events if event.get('event') == 'user']
        name = user_events[-1]['parse_data']['entities'][0]['value']
        # Gửi lại hồi đáp cho người dùng
        dispatcher.utter_message(text=f"Vâng tôi đã nhận được tên bạn là {name}, vui lòng cho biết mã số nhân viên của bạn")


class ActionProvideWeekdayChoices(Action):
    def name(self) -> Text:
        return "action_provide_weekday_set_meeting_room"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_events = [event for event in tracker.events if event.get('event') == 'user']


        name = user_events[-2]['parse_data']['entities'][0]['value']
        em_id = user_events[-1]['parse_data']['entities'][0]['value']
        # Danh sách các nút chọn
        choices = [
            {"title": "Chủ Nhật", "payload": f"Bạn {name} với mã nhân viên là {em_id} đã chọn Chủ Nhật"},
            {"title": "Thứ Hai", "payload": f"Bạn {name} với mã nhân viên là {em_id} đã chọn Thứ Hai"},
            {"title": "Thứ Ba", "payload": f"Bạn đã {name} với mã nhân viên là {em_id} chọn Thứ Ba"},
            {"title": "Thứ Tư", "payload": f"Bạn đã {name} với mã nhân viên là {em_id} chọn Thứ Tư"},
            {"title": "Thứ Năm", "payload": f"Bạn đã {name} với mã nhân viên là {em_id} chọn Thứ Năm"},
            {"title": "Thứ Sáu", "payload": f"Bạn đã {name} với mã nhân viên là {em_id} chọn Thứ Sáu"},
            {"title": "Thứ Bảy", "payload": f"Bạn đã {name} với mã nhân  viên là {em_id} chọn Thứ Bảy"}
        ]

        # Gửi lại các nút chọn cho người dùng
        dispatcher.utter_message(text="Vui lòng chọn một trong các tùy chọn ngày đặt phòng sau đây:", buttons=choices)

        return []

class ActionProvideHourChoices(Action):
    def name(self) -> Text:
        return "action_provide_hour_set_meeting_room"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        keyword_en = ''
        choices = []
        keyword_name = tracker.latest_message['entities'][0]['value']
        keyword_id = tracker.latest_message['entities'][1]['value']
        keyword_weekday = tracker.latest_message['entities'][2]['value']
        if keyword_weekday == 'Chủ Nhật':
            keyword_en = 'SUN'
        elif keyword_weekday == 'Thứ Hai':
            keyword_en = 'MON'
        elif keyword_weekday == 'Thứ Ba':
            keyword_en = 'TUE'
        elif keyword_weekday == 'Thứ Tư':
            keyword_en = 'WED'
        elif keyword_weekday == 'Thứ Năm':
            keyword_en = 'THUR'
        elif keyword_weekday == 'Thứ Sáu':
            keyword_en = 'FRI'
        elif keyword_weekday == 'Thứ Bảy':
            keyword_en = 'SAT'
        list = ['7h-9h','9h-11h','13h-15h','15h-17h']
        if len(list) != 0:
            # Danh sách các nút chọn
            for i in list:
                choices.append({"title": f"{i}", "payload": f"Bạn {keyword_name} mã nhân viên {keyword_id} đã chọn khung giờ là {i} ngày {keyword_weekday}"})


            # choices = [
            #     {"title": "Chủ Nhật", "payload": "Bạn đã chọn Chủ Nhật"},
            #     {"title": "Thứ Hai", "payload": "Bạn đã chọn Thứ Hai"},
            #     {"title": "Thứ Ba", "payload": "Bạn đã chọn Thứ Ba"},
            #     {"title": "Thứ Tư", "payload": "Bạn đã chọn Thứ Tư"},
            #     {"title": "Thứ Năm", "payload": "Bạn đã chọn Thứ Năm"},
            #     {"title": "Thứ Sáu", "payload": "Bạn đã chọn Thứ Sáu"},
            #     {"title": "Thứ Bảy", "payload": "Bạn đã chọn Thứ Bảy"}
            # ]

            # Gửi lại các nút chọn cho người dùng
            dispatcher.utter_message(text=f"Hiện tại vào ngày {keyword_weekday} phòng họp còn trống các khung giờ dưới đây, vui lòng chọn thời gian bạn muốn đặt phòng họp:", buttons=choices)
        else:
            # Danh sách các nút chọn
            choices_2 = [
                {"title": "Chủ Nhật", "payload": f"Bạn {keyword_name} với mã nhân viên là {keyword_id} đã chọn Chủ Nhật"},
                {"title": "Thứ Hai", "payload": f"Bạn {keyword_name} với mã nhân viên là {keyword_id} đã chọn Thứ Hai"},
                {"title": "Thứ Ba", "payload": f"Bạn đã {keyword_name} với mã nhân viên là {keyword_id} chọn Thứ Ba"},
                {"title": "Thứ Tư", "payload": f"Bạn đã {keyword_name} với mã nhân viên là {keyword_id} chọn Thứ Tư"},
                {"title": "Thứ Năm", "payload": f"Bạn đã {keyword_name} với mã nhân viên là {keyword_id} chọn Thứ Năm"},
                {"title": "Thứ Sáu", "payload": f"Bạn đã {keyword_name} với mã nhân viên là {keyword_id} chọn Thứ Sáu"},
                {"title": "Thứ Bảy", "payload": f"Bạn đã {keyword_name} với mã nhân viên là {keyword_id} chọn Thứ Bảy"}
            ]
            dispatcher.utter_message(text=f"Xin lỗi nhưng hiện tại vào ngày {keyword_weekday} phòng họp đã được đặt ở tất cả các khung giờ, vui lòng chọn ngày khác nếu bạn muốn!", buttons=choices_2)
        return []

class ActionConfirmMeetingRoomChoices(Action):
    def name(self) -> Text:
        return "action_confirm_set_meeting_room"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("tracker: ", tracker.latest_message)
        keyword_id = tracker.latest_message['entities'][1]['value']
        keyword_hour = tracker.latest_message['entities'][2]['value']
        keyword_weekday = tracker.latest_message['entities'][3]['value']
        keyword_name = tracker.latest_message['entities'][0]['value']





        # Gửi lại các nút chọn cho người dùng
        dispatcher.utter_message(text=f"Vâng tôi xin xác nhận bạn {keyword_name} mã nhân viên {keyword_id} đã đặt phòng họp lúc {keyword_hour} vào ngày {keyword_weekday}.")

        return []

class ActionCheckAreaShowroom(Action):

    def name(self) -> Text:
        return "action_check_area_showroom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("check vị trí showroom")
        send = ''
        dict_tinh = {
            "CẦN THƠ HẬU GIANG": "công ty Cần Thơ.",
            "HỒ CHÍ MINH": "công ty An Lạc.",
            "ĐỒNG NAI": "công ty Đồng Nai. Địa chỉ:  Biên Hòa, Đồng Nai",
            "BÌNH DƯƠNG": "công ty Bình Dương. Địa chỉ:  Thuận An, Bình Dương.",
            "LÂM ĐỒNG": "công ty Lâm Đồng. Địa chỉ:  TP. Bảo Lộc, Lâm Đồng",
            "BÀ RỊA VŨNG TÀU": "công ty Vũng Tàu. Địa chỉ: TX. Phú Mỹ, Bà Rịa – Vũng Tàu",
            "BÌNH PHƯỚC": "công ty Bình Phước. Địa chỉ:  TP. Đồng Xoài, Bình Phước.",
            "TÂY NINH": "công ty Tây Ninh. Địa chỉ:  H. Gò Dầu, Tây Ninh",
            "KHÁNH HÒA": "công ty Khánh Hòa. Địa chỉ:  Xã Vĩnh Lương, TP. Nha Trang, Khánh Hòa",
            "BÌNH THUẬN": "công ty Bình Thuận. Địa chỉ:  H. Hàm Thuận Bắc, Bình Thuận.",
            "LONG AN": "công ty Long An. Địa chỉ:  H. Thủ Thừa, Long An",
            "TIỀN GIANG": "công ty Tiền Giang. Địa chỉ:  TP. Mỹ Tho, Tiền Giang",
            "ĐỒNG THÁP": "công ty Đồng Tháp. Địa chỉ: Xã An Bình, H. Cao Lãnh, Đồng Tháp",
            "BẾN TRE": "công ty Bến Tre. Địa chỉ: TP. Bến Tre, Bến Tre",
            "VĨNH LONG TRÀ VINH": "công ty Vĩnh Long. H. Long Hồ, Vĩnh Long",
            "SÓC TRĂNG": "công ty Sóc Trăng. Địa chỉ:  TP. Sóc Trăng, Sóc Trăng",
            "BẠC LIÊU": "công ty Bạc Liêu. Địa chỉ:  TP. Bạc Liêu, Bạc Liêu",
            "AN GIANG": "công ty An Giang. Địa chỉ:  Q. Thốt Nốt, TP. Cần Thơ",
            "KIÊN GIANG": "công ty Kiên Giang. Địa chỉ:  TP. Rạch Giá, Kiên Giang.",
            "CÀ MAU": "công ty Cà Mau. Địa chỉ:  TP. Cà Mau, Cà Mau",
            "ĐÀ NẴNG": "công ty Đà Nẵng. Địa chỉ 1:  H. Hòa Vang, TP. Đà Nẵng",
            "QUẢNG NGÃI": "công ty Quảng Ngãi. Địa chỉ:  TP. Quảng Ngãi, Quảng Ngãi",
            "PHÚ YÊN": "công ty Phú Yên. Địa chỉ:  TP. Tuy Hòa, Phú Yên",
            "QUẢNG NAM": "công ty Quảng Nam. Địa chỉ: TP. Tam Kỳ, Quảng Nam",
            "THỪA THIÊN HUẾ": "công ty Huế. Địa chỉ:  TP. Huế, Thừa Thiên Huế",
            "BÌNH ĐỊNH": "công ty Bình Định. Địa chỉ:  TP. Quy Nhơn, Bình Định",
            "ĐẮC LẮC ĐẮK LẮK ĐẮC NÔNG ĐẮK NÔNG ĐĂC NÔNG ĐĂK NÔNG": " TP. Buôn Ma Thuột, Đak Lak",
            "KON TUM": "công ty Kon Tum. Địa chỉ TP. Kon Tum, Kon Tum",
            "GIA LAI": "công ty Gia Lai. Địa chỉ:  TP.  Pleiku, Gia Lai",
            "QUẢNG TRỊ": "công ty Quảng Trị. Địa chỉ: huyện Triệu Phong, tỉnh Quảng Trị.",
            "QUẢNG BÌNH": "công ty Quảng Bình. Địa chỉ: TP. Đồng Hới, Quảng Bình",
            "THỦ ĐÔ HÀ NỘI": "công ty Hà Nội. Địa chỉ: Q. Thanh Trì, Hà Nội. 3. ",
            "HẢI PHÒNG": "công ty Hải Phòng. Địa chỉ:  Hải An, Hải Phòng",
            "QUẢNG NINH": "công ty Quảng Ninh. Địa chỉ:  TP. Hạ Long, Quảng Ninh.\n công ty Trí Lực. Địa chỉ: Móng Cái, Quảng Ninh.",
            "NGHỆ AN": "công ty Nghệ An. Địa chỉ: QL1A,  Huyện Hưng Nguyên, Tỉnh Nghệ An.",
            "HÀ TĨNH": "công ty Hà Tĩnh. Địa chỉ:  huyện Thạch Hà, tỉnh Hà Tĩnh",
            "THANH HÓA": "công ty Thanh Hóa. Địa chỉ:  H. Hoằng Hóa, Thanh Hóa",
            "VĨNH PHÚC": "công ty Vĩnh Phúc. Địa chỉ: Quốc Lộ 2A, H. Yên Lạc, Vĩnh Phúc",
            "HÀ NAM": "công ty Hà Nam. Địa chỉ: Km4 QL1A,  TP. Phủ Lý, Hà Nam.",
            "HƯNG YÊN": "công ty Hưng Yên. Địa chỉ:  Huyện Văn Lâm, tỉnh Hưng Yên",
            "BẮC NINH": "công ty Bắc Ninh. Địa chỉ: TP. Bắc Ninh, Bắc Ninh.",
            "NINH BÌNH": "công ty Ninh Bình. Địa chỉ: Yên Mô, Ninh Bình.",
            "THÁI BÌNH": "công ty Thái Bình. Địa chỉ:  H. Vũ Thư, Thái Bình",
            "NAM ĐỊNH": "công ty Nam Định. Địa chỉ:  TP. Nam Định, Nam Định",
            "THÁI NGUYÊN BẮC KẠN": "công ty Thái Nguyên. Địa chỉ 1:  TP. Sông Công, Thái Nguyên. Địa chỉ 2:   TP. Thái Nguyên, Thái Nguyên.",
            "HẢI DƯƠNG": "công ty Hải Dương. Địa chỉ: TP. Hải Dương, Hải Dương.",
            "LÀO CAI": "công ty Lào Cai. Địa chỉ: TP. Lào Cai, Lào Cai.",
            "PHÚ THỌ": "công ty Phú Thọ. Địa chỉ: TP. Việt Trì, Phú Thọ",
            "YÊN BÁI": "công ty Hòa Bình - Yên Bái. Địa chỉ: Yên Bình, Yên Bái",
            "HÀ GIANG": "công ty Hà Giang. Địa chỉ: TP. Hà Giang, Hà Giang",
            "BẮC GIANG": "công ty Bắc Giang. Địa chỉ: TP. Bắc Giang, Bắc Giang",
            "ĐIỆN BIÊN": "công ty Điện Biên. Địa chỉ:  TP. Điện Biên, Điện Biên",
            "HÒA BÌNH": "công ty Hòa Bình. Địa chỉ:  TP. Hòa Bình, Hòa Bình",
            "LAI CHÂU": "công ty Lai Châu - Lai Châu. Địa chỉ:  TP. Lai Châu, Lai Châu",
            "LẠNG SƠN": "công ty Lạng Sơn. Địa chỉ: TP. Lạng Sơn, Lạng Sơn",
            "SƠN LA": "công ty Sơn La. Địa chỉ: Khu CN Chiềng Sinh, Xã Chiềng Sinh, TX. Sơn La, Sơn La",
            "TUYÊN QUANG": "công ty Tuyên Quang. Địa chỉ: TP. Tuyên Quang, Tuyên Quang"
        }
        try:
            keyword = tracker.latest_message['entities'][0]['value']
            keyword_title = keyword.title()
            keyword_upper = keyword.upper()
            print("key word vị trí tỉnh", keyword_upper)

            for key, value in dict_tinh.items():
                if (keyword_upper == key) or (keyword_upper in key):
                    send = value
                    break
                else:
                    send = "Dường như tên vị trí bạn nhập không phải là tỉnh hay thành phố trực thuộc trung ương, vui lòng kiểm tra lại và cho tôi cái tên chính xác!"

        except Exception as bug:
            send = "Vui lòng cho biết tỉnh thành phố trực thuộc trung ương nơi bạn muốn mua xe, tôi sẽ cung cấp cho bạn địa chỉ showroom công ty cụ thể!"
        # Hiển thị kết quả tìm kiếm cho người dùng
        dispatcher.utter_message(f"{send}")

        return []

class ActionCalculate(Action):

    def name(self) -> Text:
        return "action_calculate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sentence = tracker.latest_message['text']
        send = calculate(sentence)
        # Hiển thị kết quả tìm kiếm cho người dùng
        dispatcher.utter_message(f"{send}")

        return []

# class InMemoryTrackerStore(TrackerStore, SerializedTrackerAsText):
#     def __init__(domain: Domain,
#                  event_broker: Optional[EventBroker] = None,
#                  **kwargs: Dict[Text, Any]) -> None:
#
#     async def save(tracker: DialogueStateTracker) -> None:
#
#     async def retrieve(sender_id: Text) -> Optional[DialogueStateTracker]:
#
#     async def keys() -> Iterable[Text]:
#
#     async def retrieve_full_tracker(
#                 sender_id: Text) -> Optional[DialogueStateTracker]:

class ActionSendJson(Action):

    def name(self) -> Text:
        return "action_send_json"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        keyword = tracker.latest_message['entities'][0]['value']
        keyword_upper = keyword.upper()
        print("key word su menh", keyword_upper)
        send = ''
        for key, value in dict_company.items():
            if keyword_upper == key:
                send = dict_company['công ty']['MISSION']
                break
            elif (keyword_upper in key) and (keyword_upper != key):
                send = dict_company[key]['MISSION']
                break
        # Hiển thị kết quả tìm kiếm cho người dùng
        dispatcher.utter_message(f"{send}")

        return []


