#Continue statement

for i in range(10):
    if(i%2==0):
        pass
    else:
        print(i)

for i in range(10):
    if(i%2==0):
        continue
    else:
        print(i,end=" ")
print()
