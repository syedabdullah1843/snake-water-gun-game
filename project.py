import random

computer = random.choice([-1,0,1])
playerstr = input("Enter your choice: ")
playerDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0:"Gun"}

player = playerDict[playerstr]

print(f"Player chose {reverseDict[player]}\n Computer chose {reverseDict[computer]}")

if(computer == player):
    print("Its draw")
else:
    if(computer ==-1 and player == 1):
        print("player win!")
    elif(computer ==-1 and player ==0):
        print("player lose!")
    elif(computer ==1 and player ==-1):
        print("player lose!")
    elif(computer ==1 and player ==0):
        print("player win!")
    elif(computer ==0 and player ==-1):
        print("player win!")
    elif(computer ==0 and player ==1):
        print("player lose!")
    else:
        print("Somthing is wrong!")
    