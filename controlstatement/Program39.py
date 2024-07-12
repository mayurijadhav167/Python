
Playerlist=["Rohit","Subman","Virat","Ayyar","KLRahul"]
PlayerName=input("Enter Player name:")

count=0

for Player in Playerlist:

    count=count+1

    if Player==PlayerName:
        print(PlayerName,"Present in list")
        break
print("count=",count)
