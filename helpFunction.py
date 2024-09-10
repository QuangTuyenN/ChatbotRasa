import requests
import datetime
from bs4 import BeautifulSoup
from time import sleep
def current_weather(city):
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"  # Đường dẫn trang web để lấy dữ liệu về thời tiết
    #city=input(str("Chọn thành phố: "))
    if not city:  # nếu biến city != 0 và = False thì để đấy ko xử lí gì cả
        pass
    api_key = "7b078783b30065e328997afde0bbf77d"  # api_key lấy trên open weather map  "321736900281f24ef0a888c9112b0758"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric" + "&lang=vi" # tìm kiếm thông tin thời thời tiết của thành phố
    # truy cập đường dẫn lấy dữ liệu thời tiết
    response = requests.get(call_url)
    data = response.json()  # lưu dữ liệu thời tiết dưới dạng json và cho vào biến data
    #print("==========",data)
    if data["cod"] != "404":  # kiểm tra nếu ko gặp lỗi 404 thì xem xét và lấy dữ liệu
        city_res = data["main"]
        #print("city_res",city_res)
        current_temperature = city_res["temp"]
        max_temperature = city_res["temp_max"]
        min_temperature = city_res["temp_min"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        city = city.title()
        content = f"""
        Thời tiết tại {city}:
        Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}
        Mặt trời mọc vào {sunrise.hour} giờ {sunrise.minute} phút
        Mặt trời lặn vào {sunset.hour} giờ {sunset.minute} phút
        Nhiệt độ trung bình là {current_temperature} độ C
        Áp suất không khí là {current_pressure} héc tơ Pascal
        Độ ẩm là {current_humidity}%
        Thời tiết {weather_description}
        """
        #print(content)
        return content
    else:
        #print("Không tìm thấy địa chỉ của bạn")
        return "Xin lỗi"

def crawl_gold():
    url = "http://giavang.doji.vn/trangchu.html"
    response = requests.get(url)
    print("res vàng ", response)
    sleep(1)
    soup = BeautifulSoup(response.content, 'html.parser')
    div_tags = soup.find_all('div')
    for div_tag in div_tags:
        h2Tag = div_tag.find_all("h2")
        if len(h2Tag) > 0:
            h2_tag = div_tag.find('h2')
            if h2_tag.text.strip()=="Bảng giá tại Đà Nẵng":
                div_tag=div_tag.find_next_sibling()
                if div_tag is not None:
                    tbody = div_tag.find('tbody')
                    rows = tbody.find_all('tr')
                    result = {}
                    # Duyệt qua từng dòng và tạo key-value tương ứng trong dictionary
                    for row in rows:
                        # Lấy tất cả các ô của dòng hiện tại
                        cells = row.find_all('td')
                        # Lấy nội dung của ô đầu tiên làm key
                        key = cells[0].text.strip()
                        # Lấy nội dung của các ô còn lại làm value
                        values = [cell.text.strip() for cell in cells[1:]]
                        # Tạo key-value tương ứng trong dictionary
                        result[key] = {
                            'Mua vào': values[0],
                            'Bán ra': values[1]
                        }
                    # In kết quả
                    return result
def money_question(money):
    #money=input(str("Câu hỏi về tiền tệ : "))     #Giá đô la mỹ là bao nhiêu
    print("money ", money)
    url = "https://www.google.com/search?q=" + f"tỷ giá {money} sang vnd"
    sleep(1)
    response=requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        info = soup.find('div', attrs={"class": "BNeawe"})         #BNeawe s3v9rd AP7Wnd
        delTagInfo = info.text
        mainData = info.find("span", attrs={"class": "FCUp0c"}).text
        # print("del",delTagInfo)
        # print("main",mainData)
        # print("1")
        return delTagInfo
    except:
        info = soup.find('div', attrs={"class": "BNeawe"})
        delTagInfo = info.text
        # print("del2",delTagInfo)
        # print("2")
        try:
            mainData = info.find("span", attrs={"class": "FCUp0c"}).text
            # print("3")
            # print("main3",mainData)
            return mainData
        except:
            print("4")
            print("del4",delTagInfo)
            return delTagInfo
def read_news():
    queue = input(str("Content: "))
    linkAPI=f'https://newsapi.org/v2/everything?q={queue}&sortBy=popularity&language=vi&apiKey=d282bcf44dd54677aa6612bf2f1a9a8f'
    api_result = requests.get(linkAPI)
    api_response = api_result.json()
    print("Tin tức")

    for number, result in enumerate(api_response['articles'], start=1):
        if number <5:
            news=f"Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}"
            #print(f"Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}")
    return news

def today_news():
    url = 'https://vnexpress.net/thoi-su'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    sleep(1)
    article_titles = soup.find_all('h3', class_='title-news')
    article_links = [title.find('a')['href'] for title in article_titles]
    count = 0
    content = ""
    # Print the titles and links
    for i, title in enumerate(article_titles):
        # print(f'{i + 1}. {title.text.strip()}')
        # print(f'   Link: {article_links[i]}\n')
        content=content + f"""{i + 1}. {title.text.strip()}\n Link: {article_links[i]}\n"""
        count = count + 1

        if count == 5:
            break
    return content

