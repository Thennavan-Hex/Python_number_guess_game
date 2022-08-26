import random
print("\n\t\tWelcome to the game Number Guessing Game\t\t \n")
ent=input("Press y to Continue...")
num = random.randint(1, 100)
if ent=="y":
    n=0
    print("Guess the number between 1 to 100")
    if num<0:
        print("enter number is wrong")
    else:
        while n<5:
            t=int(input("Guess:"))
            if t<num:
                print(" Your guess number is lower")
            elif t==num:
                print("Correct")
            else:
                print("Your guess number is higher")
            n+=1
print("The number is ",num)