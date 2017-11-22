import random
chance = random.randint(0,8)
def fortunes(chance):
    fortunelist = [
    "\nYou will be rich, Russian rich.\n",
    "\nYou will be sloth, Russian sloth.\n",
    "\nYou will be jerk, Russian jerk.\n",
    "\nYou will be good person.\n",
    "\nYou will be......\n",
    "\nYou will help those who need it...... nah. Screw that.\n ",
    "\nYou will be cancer.\n",
    "\nYou will be troll.\n",
    "\nYou will die tomorrow.\n"
    ]
    return fortunelist[chance]


def main():
    print("Hello there, welcome to Russian Magic 8 Ball. \nGive me your name, NOW!.")
    name = str(input())
    result = fortunes(chance)
    print(result)

main()
