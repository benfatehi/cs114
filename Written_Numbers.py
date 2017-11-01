print("Hello, welocme to Written Numbers. \nPlease give me a whole number between 1 and 99.")
number=int(input())
ones = number % 10
tens = number // 10
if tens == 2:
    output = 'Twenty'
elif tens == 3:
    output = 'Thirty'
elif tens == 4:
    output = 'Forty'
elif tens == 5:
    output = 'Fifty'
elif tens == 6:
    output = 'Sixty'
elif tens == 7:
    output = 'Seventy'
elif tens == 8:
    output = 'Eighty'
elif tens == 9:
    output = 'Ninety'

if ones == 1:
    output = 'one'
elif ones == 2:
    output = 'two'
elif ones == 3:
    output = 'three'
elif ones == 4:
    output = 'four'
elif ones == 5:
    output = 'five'
elif ones == 6:
    output = 'six'
elif ones ==7:
    output = 'seven'
elif ones ==8:
    output = 'eight'
elif ones == 9:
    output = 'nine'

if tens == 0:
    output=ones
elif tens == 1:
    if ones == 1:
        output = 'Eleven'
    elif ones == 2:
        output = 'Twelve'
    elif ones == 3:
        output = 'Thirteen'
    elif ones == 5:
        output = 'Fifteen'
else:
    output = ones + '-teen'
