  const intToChar = {
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
  }

  let result = '';
  let current = number;

  while (current > 0) {
    if (current in intToChar) {
      result = intToChar[current] + result;
      current -= current;
    } else {
      let key = Object.keys(intToChar).find(k => current - k > 0);
      result = intToChar[key] + result;
      current -= key;
    }
  }

  return result;
}



