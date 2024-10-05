  const roman_numerals = {
    1: 'i',
    4: 'iv',
    5: 'v',
    9: 'ix',
    10: 'x',
    40: 'xl',
    50: 'l',
    90: 'xc',
    100: 'c',
    400: 'cd',
    500: 'd',
    900: 'cm',
    1000: 'm',
  }

  let result = '';
  for (const [digit, roman] of Object.entries(roman_numerals)) {
    while (number >= digit) {
      result += roman;
      number -= digit;
    }
  }

  return result;
}



