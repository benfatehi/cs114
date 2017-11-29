import random
print("Russian voice: Hello, and welcome to Russian Space Dungeon.")

hp = 10
mp = 10

while (mp > 0) == True:
    print("Russian voice: You have", mp, " magic points")
    mp -= random.randint(1,10)



for attack in range(5):
    random_damage = random.randint(1,10)
    print(hp)
    print("Russian voice: You were attacked by a were-DonaldTrump", random_damage, " damage.")
    hp -= random_damage
