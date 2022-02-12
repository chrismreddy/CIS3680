score = int(input("Please enter the score: "))

if score >= 0 and score <= 100:
    print("Converting to letter grade.")
    if score >= 90:
        print("Grade = A")
    elif score >= 80:
        print("Grade = B")
    elif score >= 70:
        print("Grade = C")
    elif score >= 60:
        print("Grade = D")
    else:
        print("Grade = F")
else:
    print("Bad score, try again.")