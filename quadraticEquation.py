# solving quadratic equation method 1 without using sqrt
a=int(input("Enter value for a:"))
b=int(input("Enter value for b:"))
c=int(input("Enter value for c:"))
part1=(b*b)-(4*a*c)
part2=part1**0.5
part3=2*a
x=((-b)+(part2))/part3
y=((-b)-(part2))/part3
print("X = ",x)
print("Y = ",y)

# solving quadratic equation method 2 using sqrt
import cmath
a=int(input("Enter value for a:"))
b=int(input("Enter value for b:"))
c=int(input("Enter value for c:"))
part1=(b*b)-(4*a*c)
part2=cmath.sqrt(part1)
part3=2*a
x=((-b)+(part2))/part3
y=((-b)-(part2))/part3
print('X = {0} \n Y = {1}'.format(x,y))