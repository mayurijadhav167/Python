
#else suit

Playerlist=["Rohit","Virat","Shubman","Ayyar","KLRahul"]
PlayerName=input("Enter Player Name:")

for Player in Playerlist:

    if Player==PlayerName:
        print(PlayerName,"Present in list")
    else:
        print(PlayerName,"Not present in list")
