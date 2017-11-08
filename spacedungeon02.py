print("Hello, and WELCOME to the Magi-Nation; the world of wonder and magic!")
print("You have 50 magic points or mp to begin with.")
mp=50
ap=50
i=5
while mp > 0 and ap > 0:
    if answer=='m':
        while mp > 0:
            print("A monster appears. Quick, cast a spell by typing, 'm'.")
            answer = input()
            mp = mp - 10
            print("You now have" , mp , "remaining.")
            print("You casted a spell and beat the monster. Congratulations!")
    elif answer=='a':
        for i in range(5):
            while ap > 0:
                ap = ap - 10
                print("you now have" , ap , "remaining.")
                print("You attacked and beat the monster. Congratulations!")
    else:
        print("Please type 'm' or 'a'.")
