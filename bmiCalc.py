#This is a BMI calculator and will receive wight and hight and show if you are in healty conditions.
#The resulting number indicates one of the following categories:
#Underweight = less than 18.5
#Normal = more or equal to 18.5 and less than 25
#Overweight = more or equal to 25 and less than 30
#Obesity = 30 or more

wight = float(input())
height = float(input())

bmi = weight/height**2
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else : print("Obesity")
