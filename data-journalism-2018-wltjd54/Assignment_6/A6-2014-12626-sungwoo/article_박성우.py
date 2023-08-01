from crawler_박성우 import Crawler

class ArticleTEMP(object):

    GENERIC   = 1
    HIGH_TEMP = 2
    LOW_TEMP  = 3
    STILL_COLD = 4

    def __init__(self, template_temp, address, w_events):
        self.template = template_temp
        self.address = address
        self.temp = w_events

    def generate_temp(self):
        if self.template == self.HIGH_TEMP:
            article_temp = "오늘은 날씨가 덥겠습니다. {}시 현재 {}의 온도는 섭씨 {}도, 습도는 {}% 입니다.".format(self.temp.time_observation.hour,
                                    self.address,
                                    self.temp.temp,
                                    self.temp.humidity)
        elif self.template == self.LOW_TEMP:
            article_temp = "{}월 {}일, {}의 온도는 섭씨 {}도로 지난 주에 급속하게 찾아온 한파의 영향으로 영하권의 추운 날씨가 계속되고 있습니다.".format(self.temp.time_observation.month,
                                    self.temp.time_observation.day,
                                    self.address,
                                    self.temp.temp)
        elif self.template == self.STILL_COLD:
            article_temp = "{}월 {}일, {}의 온도는 섭씨 {}도로 여전히 추운 날씨가 계속되고 있습니다.".format(self.temp.time_observation.month,
                                    self.temp.time_observation.day,
                                    self.address,
                                    self.temp.temp)
        elif self.template == self.GENERIC: #GENERIC
            article_temp = "{}월 {}일 {}시 현재, {}의 온도는 섭씨 {}도, 습도는 {}%입니다. 가벼운 옷차림으로 외출하셔도 좋을 것 같습니다.".format(self.temp.time_observation.month,
                                    self.temp.time_observation.day,
                                    self.temp.time_observation.hour,
                                    self.address,
                                    self.temp.temp,
                                    self.temp.humidity)
        return article_temp

class ArticleDUST(object):

    HIGH_DUST = 5
    LOW_DUST  = 6
    DUST_GOOD = 7

    def __init__(self, template_dust, address, d_events):
        self.template = template_dust
        self.address = address
        self.dust = d_events

    def generate_dust(self):
        if self.template == self.HIGH_DUST:
            article_dust = "오늘 미세먼지의 농도는 {}로 매우 높습니다. 불필요한 외출을 삼가하시기 바랍니다.".format(self.dust.dust_value)
        elif self.template == self.LOW_DUST:
            article_dust = "현재 {}에서 측정한 미세먼지의 농도는 {}으로 '{}'수준입니다. 외출을 하시려면 반드시 마스크를 착용하세요.".format(
                                    self.dust.location,
                                    self.dust.dust_value,
                                    self.dust.dust_grade)
        elif self.template == self.DUST_GOOD:
            article_dust = "{}에서 측정한 미세먼지의 농도는 {}으로 '{}'수준입니다. 오늘 같은 날은 마음껏 외출하셔도 좋을 듯합니다.".format(
                                    self.dust.location,
                                    self.dust.dust_value,
                                    self.dust.dust_grade)
        return article_dust

class ArticleMovie(object):

    def generate_movie(self):
        crawling = Crawler()
        box_office = crawling.daily_movie()
        box_office_list = []
        for movies in box_office:
            box_office_list.append(movies[1])
        box_office_chart = ', '.join(box_office_list)
        article_movie = "현재 박스오피스 1위부터 10위까지의 순위는 " + box_office_chart + "와 같으며, 이 가운데 현재 1위인 {}는 {}명의 관객을 동원했습니다.".format(box_office[0][1], box_office[0][0])
        return article_movie

class ArticleTwitter(object):

    def generate_twitter(self):
        crawling = Crawler()
        id = 'RVsmtown'
        twitter = crawling.twitter(id)
        article_twitter = "관심있으신 {}의 가장 최근 업데이트된 트윗은: {}입니다.".format(id, twitter)
        return article_twitter