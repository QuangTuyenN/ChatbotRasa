import wolframalpha
from googletrans import Translator
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
client = wolframalpha.Client('L359HX-XA3644KE92')
translator = Translator()


def calculate(sentence):
    try:
        query_en = translator.translate(sentence, src='vi', dest='en').text
        # print("query_en",query_en)
        res = client.query(query_en)
        output = next(res.results).text

        output_vi = translator.translate(output, src='en', dest='vi').text
    except:
        output_vi = "Xin lỗi nhưng phép tính quá phức tạp, tôi không thể đưa ra kết quả chính xác"
    return output_vi

