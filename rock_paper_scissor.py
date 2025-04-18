import random
'''
1 for paper
-1 for scissor
0 for rock
'''
computer= random.choice([0,-1,1])
youstr=input("Enter your choice:")
youDict={"p":1, "s":-1,"r":0}
reverseDict={1:"Paper", -1: "Scissor", 0:"Rock"}

you=youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("Match Draw.")

else:
    if(computer==0 and you==1):
        print("You Win!")
    
    elif(computer==0 and you == -1):
        print("Computer Win!\nYou Lose.")

    elif(computer==1 and you==0):
        print("Computer Win!\nYou Lose.")

    elif(computer==1 and you==-1):
        print("You Win!.")

    elif(computer==-1 and you==0):
        print("You Win!")

    elif(computer==-1 and you==1):
        print("Computer Win!\nYou Lose.")

    else:
        print("Something is wrong.")
    
