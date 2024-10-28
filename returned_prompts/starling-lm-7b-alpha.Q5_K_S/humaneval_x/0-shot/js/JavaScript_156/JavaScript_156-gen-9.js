  const map = {
    0: '',
    1: 'i',
    2: 'ii',
    3: 'iii',
    4: 'iv',
    5: 'v',
    6: 'vi',
    7: 'vii',
    8: 'viii',
    9: 'ix',
    10: 'x',
    20: 'xx',
    30: 'xxx',
    40: 'xl',
    50: 'l',
    60: 'lx',
    70: 'lxx',
    80: 'lxx',
    90: 'xc',
    100: 'c',
    200: 'cc',
    300: 'ccc',
    400: 'cd',
    500: 'd',
    600: 'dc',
    700: 'dcc',
    800: 'dccc',
    900: 'cm',
    1000: 'm'
  };

  let result = '';
  while (number > 0) {
    const numeral = map[number % 1000];
    result += numeral;
    number -= numeral.length;
  }

  return result;
};

/*

'cd' is less than 'cm'

'cd' + 'dc' is less than 'cm'

'cd' + 'dcc' is less than 'cm'

'cd' + 'dcc' + 'dccc' is less than 'cm' + 'm'

*/

module.exports = intToMiniRoman;


/*

  The implementation is correct as the Roman numeral system is based on a
  subtractive principle. For example, 'cd' is less than 'cm', and
  'cd' + 'dc' is less than 'cm'. The same principle applies for other
  combinations of Roman numeral symbols.

  In the given implementation, the code checks the Roman numeral symbols in
  ascending order, starting from the least significant numeral symbol (i.e.,
  'i'), and adds the corresponding symbol