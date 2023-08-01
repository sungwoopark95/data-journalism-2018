from crawler_박성우 import Crawler
from events_박성우 import Events
from mood_detect_박성우 import Mood
import article_박성우

crawler = Crawler()

# 데이터 수집
weather_data = crawler.weather_fetch("Busan")
fine_dust_data = crawler.fine_dust_fetch("연산동")

# print(weather_data)
# print(fine_dust_data)

# 날씨 이벤트 처리
weather_events = Events(weather_data, Events.WEATHER)
weather_events.process_events()

# 미세먼지 이번트 처리
dust_events = Events(fine_dust_data, Events.FINE_DUST)
dust_events.process_events()

# 데이터 체크
# print(weather_events.temp)
# print(dust_events.dust_grade)


# Mood detection을 위한 날씨 정보 데이터 구축
temp_info = weather_events.temp
dust_info = dust_events.dust_value
address = dust_events.location

# Mood decision
mood = Mood()
template_temp = mood.decision_temp(temp_info)
template_dust = mood.decision_dust(dust_info)
# print(template_temp)
# print(template_dust)

# 기사 생성
article_temp = article_박성우.ArticleTEMP(template_temp, address, weather_events)
article_dust = article_박성우.ArticleDUST(template_dust, address, dust_events)
article_movie = article_박성우.ArticleMovie()
article_twitter = article_박성우.ArticleTwitter()
article = article_temp.generate_temp() + '\n' + article_dust.generate_dust() + '\n' + article_movie.generate_movie() + '\n' + article_twitter.generate_twitter()
print(article)

# 기사 텍스트 파일 생성
with open('article_박성우.txt', 'w', encoding='utf-8') as file:
    news = file.write(article)
