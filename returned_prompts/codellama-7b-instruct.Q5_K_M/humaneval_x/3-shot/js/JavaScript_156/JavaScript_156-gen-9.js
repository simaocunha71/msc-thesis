  const roman = {
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
  var result = '';
  while (number > 0) {
    for (const [key, value] of Object.entries(roman)) {
      if (number >= key) {
        result += value;
        number -= key;
        break;
      }
    }
  }
  return result;
}



