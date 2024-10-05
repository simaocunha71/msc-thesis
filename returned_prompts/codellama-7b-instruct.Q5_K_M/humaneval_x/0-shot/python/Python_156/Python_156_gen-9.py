
def int_to_mini_roman(number):
    roman_nums = {
        1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'
    }
    mini_roman = ''
    for num, roman in roman_nums.items():
        while number >= num:
            mini_roman += roman
            number -= num
    return mini_roman
