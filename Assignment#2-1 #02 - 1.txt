def temperature(): # 온도를 입력받기 때문에 미리 집어넣을 매개변수가 없음
    cel = int(input("온도를 입력하십시오: "))
    fah = ((9 / 5) * cel) + 32
    print("섭씨 %d도는 화씨로 %d도 입니다." % (cel, fah))
    # 매개변수가 없기 때문에 return값도 없음

temperature() # 함수가 print로 끝났기 때문에 print할 값이 없음