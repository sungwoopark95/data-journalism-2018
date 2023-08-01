def temperature_c(tem): 
    fah = round(((9 / 5) * tem) + 32,2)
    print("섭씨 %.2f도는 화씨로 %.2f도 입니다." % (tem, fah))

def temperature_f(tem):
    cel = round((5 / 9) * (tem - 32), 2)
    print("화씨 %.2f도는 섭씨로 %.2f도 입니다." % (tem, cel))

temperature_c(31.7)
temperature_f(65.3)