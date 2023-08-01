gugudan = open("gugudan.txt", "w")

for i in range(2,10):
    for j in range(1,10):
        gugudan.write("%d * %d = %d\n" % (i, j, i*j))
    if i < 9:
        gugudan.write("\n")

gugudan.close()