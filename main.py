a = 10
b = 12
c = 0
if a and b and c:
    print("all the numbers have boolean value as true")
else:
    print("alteast one number has boolean value as false")



a = 10 
b = -10
c = 0
if b > 0 or c > 0:
    print("either of the number is greater than 0")
else:
    print("no number is greater than 0")
a = 10 
b = 12
c = 2
print( a != b)
print( b != c)
a = "python"
b = "coding"
if a != b :
    print("a and b are different")
a = 4
b = 5
if ( a == 1) != (b == 5):
    print('hello')

a = int(input("enter a number"))
if a%2 != 0:
    print("a, is not even a number.")
height = float(input("enter your height in cm")
weight = float(input("enter your weight in kg")
BMI = weight / (height/100)**2
print("your BMI is",BMI)
if BMI <= 18.4:
    print("you are underweight")
elif BMI <= 24.9:
    print("you are healthy.")
elif BMI <= 29.9:
    print("you are overweight.")
elif BMI <= 34.9:
    print("you are severly overweight.")
elif BMI <= 39.9:
    print("you are obese.")
else BMI <= 44.9:
    print("you are severly obese.")
a = 5
b = 10
c = 20
a = a + b + c
b = a - (b + c)
c = a - (b +c)
a = a - (b + c)
print(a,b,c)
