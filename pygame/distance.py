import math

print("enter the x cordinate of first point")
x1=int(input("value is:"))
print("enter the y coordinate of first point")
y1=int(input("value is:"))

print("enter the x cordinate of second point")
x2=int(input("value is:"))
print("enter the y coordinate of second point")
y2=int(input("value is:"))

d=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

print('distance between two points is:',d)

