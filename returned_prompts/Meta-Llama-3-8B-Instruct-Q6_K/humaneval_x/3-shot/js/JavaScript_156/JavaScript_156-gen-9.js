  const roman_numerals = {
    1000: 'm',
    900: 'cm',
    500: 'd',
    400: 'cd',
    100: 'c',
    90: 'xc',
    50: 'l',
    40: 'xl',
    10: 'x',
    9: 'ix',
    5: 'v',
    4: 'iv',
    1: 'i'
  };

  let result = '';
  for (let value in roman_numerals) {
    while (number >= parseInt(value)) {
      result += roman_numerals[value];
      number -= parseInt(value);
    }
  }
  return result.toLowerCase();
}