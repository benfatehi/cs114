import random
input("\nWelcome to Villains fight! Press enter to start.\n")

def villains():
    chance = random.randint(0,3)
    enemy = ["Thanos", "Surtur", "Galactus", "Darkseid"]
    if chance==0:
        print(enemy[chance], "has appeared.")
    elif chance==1:
        print(enemy[chance], "has appeared.")
    elif chance==2:
        print(enemy[chance], "has appeared.")
    elif chance==3:
        print(enemy[chance], "has appeared.")

villains()
