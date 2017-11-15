import random
def fortunes(number):
    if number==1:
        return "You will be rich, Russian rich."
    elif number==2:
        return "You will be sloth, Russian sloth."
    elif number==3:
        return "You will be jerk, Russian jerk."
    elif number==4:
        return "You will be good person."
    elif number==5:
        return "You will be......"
    elif number==6:
        return "You will help those who need it...... nah. Screw that. "
    elif number==7:
        return "You will be cancer."
    elif number==8:
        return "You will be troll."
    elif number==9:
        return "You will die tomorrow."

def main():
    print("Hello there, welcome to Russian Magic 8 Ball. \nGive me your name, NOW!.")
    name = input()
    number2 = random.randint(1,9)
    result = fortunes(number2)
    print (result)

main()
