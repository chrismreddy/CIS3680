LBS_PER_KG = 2.2046
INCHES_PER_METER = 39.3701

def calc_bmi(weight_kg, height_m):
    return weight_kg / height_m**2

def input_float(prompt, min_value = None):
    done = False
    while not done:
        try:
            txt = input(prompt)
            value = float(txt)
            if min_value == None or min_value <= value:
                done = True
            else:
                print(f"Error: Number must be > {min_value}")
        except ValueError:
            print("That was not a number, please try again.")

    return value        

def main():
    done = False
    while not done:
        weight_lbs = input_float("Please enter weight (pounds): ", min_value = 0)
        height_in = input_float("Please enter height (inches): ", min_value = 0)

        weight_kg = weight_lbs / LBS_PER_KG
        height_m = height_in / INCHES_PER_METER

        bmi = calc_bmi(weight_kg, height_m)

        if bmi > 32:
            print("Overload situation, shutdown for maint.")
            done = True
            continue

        print(f"BMI is {bmi:.1f}")
        again = input("Go again (y/n)? ")
        if again != "y":
            done = True

if __name__ == '__main__':
    main()
