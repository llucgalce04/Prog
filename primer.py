from math import *
#Ejercicio 1
a = 3
b = 4
c = 5

result = (b**2)-4*a*c
print("The discriminatn is: ", result)

#Ejercicio 2

finalVelocity = 10.5
inicialVelocity = 5.6
time = 0.5

accelerationResult = (finalVelocity-inicialVelocity)/time
print("The avarage acceleration is ", accelerationResult)

#Ejercicio 3

width = 4.25
height = 7.26

perimeter = (width*2) + (height*2)
area = (width * height)
diagonal = ((width**2) + (height**2))**0.5

print("The perimeter of the rectangle is:", perimeter, "and the area is:", area, "and finally the diagonal of the rectangle is:", diagonal)

#Ejercicio 4

numberMonths = 60
anualInterest = (4.25/100)/12
finalValue = 1000
initalDeposit = (finalValue)/((1 + anualInterest)**numberMonths)
print("The inital deposit is ", initalDeposit)
