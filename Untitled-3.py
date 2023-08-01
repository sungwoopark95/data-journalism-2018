def cen_to_in(cm):
    result =[]
    inch = round(2.54 * cm, 2)
    result.append(cm)
    result.append(inch)
    return result

print(str(cen_to_in(31.8)[0]) + "센티미터는 " + str(cen_to_in(31.8)[1]) + "인치입니다.")