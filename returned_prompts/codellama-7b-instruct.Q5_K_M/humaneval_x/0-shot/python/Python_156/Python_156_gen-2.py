
def int_to_mini_roman(number):
    roman = ''
    for i in range(number):
        if i % 10 == 9:
            roman += 'x'
        elif i % 10 == 4:
            roman += 'v'
        elif i % 10 == 0:
            roman += 'c'
        elif i % 10 == 5:
            roman += 'd'
        elif i % 10 == 1:
            roman += 'x'
        elif i % 10 == 2:
            roman += 'x'
        elif i % 10 == 3:
            roman += 'x'
        elif i % 10 == 6:
            roman += 'c'
        elif i % 10 == 7:
            roman += 'd'
        elif i % 10 == 8:
            roman += 'd'
    return roman


