def cen_to_in(cm):
    inch = round(2.54 * cm, 2)
    print("%.2f센티미터는 %.2f인치입니다." % (cm, inch))

def in_to_cen(inch):
    cm = round((1 / 2.54) * inch, 2)
    print("%.2f인치는 %.2f센티미터입니다." % (inch, cm))

cen_to_in(31.48)
in_to_cen(21.71)