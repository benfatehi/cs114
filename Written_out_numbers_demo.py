def get_number():
    print("Hello, welcome to Written Numbers. \nPlease give me a whole number between 1 and 99.")
    number=int(input())
    return number

def get_ones_digit(number):
    ones = number % 10
    return ones

def get_tens_digit(ones):
    tens = number // 10
    return tens

def tens_word(tens):
    if tens == 2:
        tens_word = 'Twenty'
    elif tens == 3:
        tens_word = 'Thirty'
    elif tens == 4:
        tens_word = 'Forty'
    elif tens == 5:
        tens_word = 'Fifty'
    elif tens == 6:
        tens_word = 'Sixty'
    elif tens == 7:
        tens_word = 'Seventy'
    elif tens == 8:
        tens_word = 'Eighty'
    elif tens == 9:
        tens_word = 'Ninety'


if ones == 1:
    ones_word = 'one'
elif ones == 2:
    ones_word = 'two'
elif ones == 3:
    ones_word = 'three'
elif ones == 4:
    ones_word = 'four'
elif ones == 5:
    ones_word = 'five'
elif ones == 6:
    ones_word = 'six'
elif ones ==7:
    ones_word = 'seven'
elif ones ==8:
    ones_word = 'eight'
elif ones == 9:
    ones_word = 'nine'

if tens == 0:
    output=ones
elif tens == 1:
    if ones == 1:
        irregular = 'Eleven'
    elif ones == 2:
        irregular = 'Twelve'
    elif ones == 3:
        irregular = 'Thirteen'
    elif ones == 5:
        irregular = 'Fifteen'
else:
    output = tens_word + ones_word
print (output)

def main():
    # takes in number outputs word of number
    number = get_number()
    ones = get_ones_digit(number)
    tens = get_tens_digit(ones)

main()
