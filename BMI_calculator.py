#Getting weight of user
weight=int(input("enter  your weight :"))
#Getting height of user
height = int(input("enter  your height :"))
#BMI calculation
bmi = weight / (height ** 2)
#using loop for comparing BMI with standard values
if bmi<18.5:
    print("underweight")
if bmi>=18.5 and bmi<25:
    print("normal weight")
if bmi>=25:
    print("overweight")


