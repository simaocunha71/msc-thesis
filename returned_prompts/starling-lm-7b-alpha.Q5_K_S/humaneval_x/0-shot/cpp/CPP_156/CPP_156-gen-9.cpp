
def int_to_mini_roman(number):
    roman = ['i', 'iv', 'v', 'ix', 'x', 'xl', 'l', 'xc', 'c', 'cd', 'd', 'cm', 'm']
    result = []
    while number > 0:
        digit = number % 10
        index = roman.index(max(roman[i] for i in range(len(roman)) if number >= roman[i]))
        result.append(roman[index] * (number // roman[index]))
        number -= roman[index] * (number // roman[index])
    return ''.join(result)


B:

function intToRoman(num: number): string {
  const roman = {
    M: 1000,
    CM: 900,
    D: 500,
    CD: 40