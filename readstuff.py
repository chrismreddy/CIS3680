
f = open("data.txt", 'r')
line = f.readline()

while line:
    x = float(line)
    if x >= 5:
        print(x)
    line = f.readline()

f.close()