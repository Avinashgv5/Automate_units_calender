#1.Write a Python program to convert Kilometers to Miles ?

def km_miles():
    kilometer = float(input("enter kilometer: " ))
    print("{} km is Equal to {} miles".format(kilometer, kilometer * 0.621))

km_miles()

#2. Write a Python program to convert Celsius to Fahrenheit?

def Celsius_to_fahr():
    celesius= float(input("enter celesius: "))
    print("{} Celsius is equal to {} fahrenheit".format(celesius,(celesius*9/5)+32))

Celsius_to_fahr()

#3. Write a Python program to display calendar?

import calendar

def calender_year():
    year=int(input("enter calender year: "))
    print(calendar.calendar(year))
calender_year()


#4. Write a Python program to solve quadratic equation?

import cmath
import math

def quadratic_func(a,b,c):

    discriminant= (b*b)-(4*a*c)

    if discriminant==0:
        r1=-b/2*a
        r2=-b/2*a
        print("roots are real",r1,r2)

    elif discriminant>0:
        r1=(-b-math.sqrt(discriminant))/2*a
        r2=(-b+math.sqrt(discriminant))/2*a
        print("roots are real and diffirent", r1, r2)

    else:
        r1 = (-b - cmath.sqrt(discriminant)) / 2 * a
        r2 = (-b + cmath.sqrt(discriminant)) / 2 * a
        print("roots are imaginary", r1, r2)

a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))

quadratic_func(a,b,c)

#5. Write a Python program to swap two variables without temp variable?

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))

def swap_number(num1,num2):
    print("Numbers before swap", num1, num2)
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    print("Numbers after swap",num1, num2)
swap_number(num1, num2)





