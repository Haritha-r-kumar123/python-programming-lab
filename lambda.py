l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
a=int(input("Enter the side of the square:"))
area=lambda l,b:(l*b)
perimeter=lambda l,b:2*(l+b)
print("The area of the rectangle:",area(l,b))
print("The perimeter of the rectangle:",perimeter(l,b))
area=lambda a:(a*a)
perimeter=lambda a:(4*a)
print("The area of the square:",area(a))
print("The perimeter of square:",perimeter(a))
