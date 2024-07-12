
x=int(input("Enter a value of x:"))
y=int(input("Enter a value of y:"))

for i in range(x,y+1):
    if(i%2==0):
        print("{} is even".format(i))
    else:
        print("{} is odd".format(i))
