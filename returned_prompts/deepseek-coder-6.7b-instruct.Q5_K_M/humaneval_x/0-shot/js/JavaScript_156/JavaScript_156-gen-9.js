  const roman = {
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
  
  let str = '';
  
  for (let i = 1000; i > 0; i = Math.floor(i / 10)) {
      while (number >= i) {
          str += roman[i];
          number -= i;
      }
      if (number >= 900 && number < 1000) {
          str += roman[900];
          number -= 900;
      }
      if (number >= 400 && number < 500) {
          str += roman[400];
          number -= 400;
      }
      if (number >= 90 && number < 100) {
          str += roman[90];
          number -= 90;
      }
      if (number >= 40 && number < 50) {
          str += roman[40];
          number -= 40;
      }
      if (number >= 9 && number < 10) {
          str += roman[9];
          number -= 9;
      }
      if (number >= 4 && number < 5) {
          str += roman[4];
          number -= 4;
      }
  }
  
  return str.toLowerCase();
};





































































































