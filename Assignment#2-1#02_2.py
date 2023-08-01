from time import sleep

def temperature():
    while True:
        zero = input("변환하시고자 하는 온도에서 0이 몇 도인가요?: ")
        if int(zero) == 0:
            print("선생님께서 변환하시고자 하는 온도는 섭씨입니다.")
            sleep(1)
            cel = float(input("변환하시고자 하는 온도를 입력해주세요: "))
            fah = round(((9 / 5) * cel) + 32, 2)
            print("섭씨 %.2f도는 화씨로 %.2f도입니다." % (cel, fah))
            break
        elif int(zero) == 32:
            print("선생님께서 변환하시고자 하는 온도는 화씨입니다.")
            sleep(1)
            fah = float(input("변환하시고자 하는 온도를 입력해주세요: "))
            cel = round((5 / 9) * (fah - 32), 2)
            print("화씨 %.2f도는 섭씨로 %.2f도입니다." % (fah, cel))
            break
        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")

temperature()