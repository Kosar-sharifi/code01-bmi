w = float(input("enter your weight:"))
h = float(input("enter your height:"))
bmi = w/(h**2)

print(f"your weight is {w} and your height is {h} so bmi is {bmi:.2f}")
print(f"your weight is {w} and your height is {h} so bmi is {round(bmi,2)}")