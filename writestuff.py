import random

f = open("data.txt", 'w')

for count in range(500):
    x = random.randint(0, 100) / 10.0
    f.write(f"{x:.1f}\n")

f.close()