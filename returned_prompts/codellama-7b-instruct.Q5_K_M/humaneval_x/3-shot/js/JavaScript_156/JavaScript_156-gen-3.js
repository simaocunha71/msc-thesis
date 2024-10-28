  const roman = {
    1: 'i',
    4: 'iv',
    5: 'v',
    9: 'ix',
    10: 'x',
    40: 'xl',
    50: 'l',
    90: 'xcix',
    100: 'c',
    400: 'cd',
    500: 'd',
    900: 'cm',
    1000: 'm',
  };

  const roman_string = [];

  while (number > 0) {
    const current_key = Object.keys(roman).find(key => key >= number);
    roman_string.push(roman[current_key]);
    number -= current_key;
  }

  return roman_string.reverse().join('');
}



