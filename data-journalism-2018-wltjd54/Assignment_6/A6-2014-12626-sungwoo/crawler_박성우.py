import urllib.request
from urllib import parse
from datetime import datetime
import json
import tweepy

class Crawler(object):

    def __init__(self, city=None, region=None):
        self.city = city      # e.g. 서울
        self.county = region    # e.g. 강남구

    def weather_fetch(self, city=None):
        self.city = city

        app_key = "35da68cb640fd015c18425f896eec5af"
        loc = self.city
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(loc, app_key)

        with urllib.request.urlopen(url) as response:
            self.weather_data = json.loads(response.read().decode("utf-8"))

        return self.weather_data

    def fine_dust_fetch(self, region=None):
        self.county = region

        app_key = "GSLrPrPc3DF0G7k%2FmjNz1rxNbMY1HHjhUGTJG4GKpL%2BGImgUjiTebNT2eWaGio8eN%2FB1NxT3N1O0A1kcyzGL0w%3D%3D"
        loc = self.county
        url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName={}&dataTerm=month&pageNo=1&numOfRows=1&ServiceKey={}&ver=1.3&_returnType=json".format(
            parse.quote(loc), app_key)
        # print(url) # check REST url

        with urllib.request.urlopen(url) as response:
            self.fine_dust_data = json.loads(response.read().decode("utf-8"))

        return self.fine_dust_data

    def daily_movie(self):

        app_key = '7885549a70b7dd271101ffe08e97c98c'
        now = datetime.now()
        yesterday = now.day - 1
        date = str(now.year) + str(now.month) + str(yesterday)
        url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={}&targetDt={}".format(
            app_key, date)

        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode("utf-8"))

        daily_chart = data['boxOfficeResult']['dailyBoxOfficeList']
        self.movie_name = []
        for movies in daily_chart:
            self.movie_name.append((movies['audiAcc'], movies['movieNm']))

        return self.movie_name

    def twitter(self, id=None):
        self.id = id
        consumer_key = 'iK6PbwIWdtHJ3VQ2Ba19PZMnQ'
        consumer_secret = 'SeGZVqjzRYd3FGHW7VOFUeSihAJHmTvl5tYse8gVpN6fAX21uJ'
        access_token = '923096752223219712-QaBkvj6hdMYmuZuzTKWjaRtPJHGqj8o'
        access_secret = 'WckTNx5CbOeIDvlImae5LCTW46XJ4tf7shtfbArNbW1Dc'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth)
        user = api.get_user(self.id)
        self.text = user.status._json['text']

        return self.text