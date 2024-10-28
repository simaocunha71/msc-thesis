  const num_to_roman = {
    1: 'i', 4: 'iv', 5: 'v', 9: 'ix',
    10: 'x', 40: 'xl', 50: 'l', 90: 'xc',
    100: 'c', 400: 'cd', 500: 'd', 900: 'cm',
    1000: 'm'
  };

  let roman = '';
  while (number) {
    for (const [num, roman_digit] of Object.entries(num_to_roman)) {
      if (number >= num) {
        roman += roman_digit;
        number -= num;
        break;
      }
    }
  }
  return roman;
}



