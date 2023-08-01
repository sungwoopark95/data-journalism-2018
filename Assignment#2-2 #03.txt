f = open("Assignment #2-2 03 - multiplation table.txt", "w")

for i in range(2,10):
    for j in range(1,10):
        f.write("%d * %d = %d\n" % (i, j, i * j))
        if j == 9:
            f.write("\n")

f.close()