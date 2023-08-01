from random import choice

list1 = ["his", "her"]
list2 = ["Mama", "Daddy"]
i = 100
while i >= 1:
    if i == 1:
        print("%d little monkey jumping on the bed." % i)
        print("One fell off and broke " + choice(list1) + " head.")
        print(choice(list2) + " called the doctor and the doctor said,")
        print('"No more monkeys jumping on the bed!"\n')
    else:
        print("%d little monkeys jumping on the bed." % i)
        print("One fell off and broke " + choice(list1) + " head.")
        print(choice(list2) + " called the doctor and the doctor said,")
        print('"No more monkeys jumping on the bed!"\n')
    i -= 1

