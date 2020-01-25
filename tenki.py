# get_rainfall.py
import requests


def main():
    url = build_url()
    json_data = request_json(url)
    in_one_hour_rainfall = extract_rainfall(json_data)

    if in_one_hour_rainfall >= 10:
        rainfall_notice = notification_level(in_one_hour_rainfall)


# url組み立て
def build_url():
    APP_ID = "dj00aiZpPU4wM2tLc1hIREZWWiZzPWNvbnN1bWVyc2VjcmV0Jng9ZDU-"
    BASE_URL = "http://weather.olp.yahooapis.jp/v1/place"
    COORDINATES = "139.709008,35.669968"  # 緯度経度
    OUTPUT = "json"

    url = BASE_URL + "?appid=%s&coordinates=%s&output=%s" % (APP_ID, COORDINATES, OUTPUT)

    return url


# リクエスト
def request_json(url):
    req = requests.get(url)
    json_data = req.json()

    return json_data


# 降水強度の取得
def extract_rainfall(json_data):
    weather = json_data['Feature'][0]['Property']['WeatherList']['Weather']
    in_one_hour_rainfall = weather[1]['Rainfall']
    print(json_data)

    return in_one_hour_rainfall


# 降水レベル
def notification_level(in_one_hour_rainfall):
    if in_one_hour_rainfall >= 80:
        return "恐怖"
    elif 50 <= in_one_hour_rainfall < 80:
        return "滝"
    elif 30 <= in_one_hour_rainfall < 50:
        return "バケツ"
    elif 20 <= in_one_hour_rainfall < 30:
        return "どしゃ"
    elif 10 <= in_one_hour_rainfall < 20:
        return "ザーザー"


if __name__ == "__main__":
    main()
