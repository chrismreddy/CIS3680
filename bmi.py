LBS_PER_KG = 2.2046
INCHES_PER_METER = 39.3701

done = False
while not done:
    weight_lbs = (input("Please enter weight (pounds): "))
    if weight_lbs == "":
        done = True
        continue

    weight_lbs = float(weight_lbs)
    height_in = float(input("Please enter height (inches): "))

    weight_kg = weight_lbs / LBS_PER_KG
    height_m = height_in / INCHES_PER_METER

    bmi = weight_kg / height_m**2

    if bmi > 32:
        print("Overload situation, shutdown for maint.")
        done = True
        continue

    print(f"BMI is {bmi:.1f}")