import random
def randomword(word):
    print ("(Russian accent): Hello and Welcome user to Russian random number generator.")
    word = input()
    num = len(word)
    result = random.randint(0, num * 2)
    return result

result = randomword('python')
print("(Russian accent): Your result is: ",result,".")
