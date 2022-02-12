from pickle import TRUE


print("Begin")

x = 0
done = False
while not done:
    print(x)
    y = int(input("Enter integer y: "))

    if y > 100:
        done = True

    x += 1
    
    if x >= 10:
        done = True

print("Done!")