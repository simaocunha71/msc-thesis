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
    1000: 'm'
  };

  let roman = '';
  let remainder = number;

  for (let value in roman_numerals) {
    while (remainder >= parseInt(value)) {
      remainder -= parseInt(value);
      roman += roman_numerals[value];
    }
  }

  return roman.toLowerCase();
}