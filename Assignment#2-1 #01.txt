family_name = input("안녕하세요. 성을 입력해주세요: ")
given_name = input("이름을 입력해주세요: ")
name = family_name + given_name
age = input(name + "님의 나이는 몇 살인가요: ")
living_sec = int(age) * 365 * 24 * 60 * 60
print("%s님은 지금까지 모두 **%d**초를 살아왔군요." % (name, living_sec))
print("지금까지 이용해주셔서 감사합니다. %s님" % name)