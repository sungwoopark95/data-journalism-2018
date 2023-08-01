starting_year = int(input("Pick a starting year (like 1973 or something): "))
print("")
ending_year = int(input("Now pick an ending year: "))
year_list = [year for year in range(starting_year, ending_year + 1)]
result = []
for year in year_list:
    # 윤년은 4로 나누어 떨어지고, 100으로 나누어 떨어지지 않는 해이거나 400으로 나누어 떨어지는 해
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        year = str(year)
        result.append(year)
print("")
print("Check it out... these years are leap years: " + " ".join(result))