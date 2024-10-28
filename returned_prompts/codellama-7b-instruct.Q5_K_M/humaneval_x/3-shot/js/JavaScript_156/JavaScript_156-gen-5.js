  const int_to_roman_map = {
    1: 'i',
    5: 'v',
    10: 'x',
    50: 'l',
    100: 'c',
    500: 'd',
    1000: 'm',
  }

  const roman_numeral = [];
  while (number > 0) {
    let [int_part, dec_part] = number.toString().split('.');
    int_part = parseInt(int_part);
    while (int_part > 0) {
      if (int_part >= 1000) {
        roman_numeral.push('m');
        int_part -= 1000;
      } else if (int_part >= 500) {
        roman_numeral.push('d');
        int_part -= 500;
      } else if (int_part >= 100) {
        roman_numeral.push('c');
        int_part -= 100;
      } else if (int_part >= 50) {
        roman_numeral.push('l');
        int_part -= 50;
      } else if (int_part >= 10) {
        roman_numeral.push('x');
        int_part -= 10;
      } else if (int_part >= 5) {
        roman_numeral.push('v');
        int_part -= 5;
      } else {
        roman_numeral.push('i');
        int_part -= 1;
      }
    }
    number = dec_part;
  }

  return roman_numeral.join('');
}
