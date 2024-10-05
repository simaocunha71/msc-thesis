  const romanNumeralMap = {
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
  };

  let result = '';

  for (const key in romanNumeralMap) {
    while (number >= key) {
      result += romanNumeralMap[key];
      number -= key;
    }
  }

  return result;
}