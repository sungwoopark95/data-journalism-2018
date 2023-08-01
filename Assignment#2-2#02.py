starting_year = int(input("시작하는 연도를 입력해주세요: "))
ending_year = int(input("끝나는 연도를 입력해주세요: "))
year_list = [year for year in range(starting_year, ending_year + 1)] # range에서 마지막 값은 항상빠지기 때문에 포함하기 위해서는 +1을 해주어야 함
result = []
for item in year_list:
    if (item % 4 == 0 and item % 100 != 0) or item % 400 == 0:
        result.append(item)
print("")
print("%d년과 %d년 사이의 윤년은 다음과 같습니다." % (starting_year, ending_year))
print(result)