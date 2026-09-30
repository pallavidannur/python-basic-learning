import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
# calculate the discriminant  
d = (b**2) - (4*a*c)  
# find two solutions  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))



num = 30
sum_of_numbers = 0
while num > 0:
    sum_of_numbers += num
    num -= 1
print("The sum is",sum_of_numbers)




