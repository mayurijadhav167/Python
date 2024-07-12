# Assert

name=input("Enter your name:")
age=int(input("Enter your age:"))

assert age>0,"...age is negative"

if age>18:
    print(name,"eligible for voting")

else:
    print(name,"not eligible for voting")
