  const roman_map = {
    1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
  };
  let roman = '';
  for (let i = 1000; i > 0; i /= 10) {
    while (number >= i) {
      number -= i;
      roman += roman_map[i];
    }
  }
  return roman.toLowerCase();
}