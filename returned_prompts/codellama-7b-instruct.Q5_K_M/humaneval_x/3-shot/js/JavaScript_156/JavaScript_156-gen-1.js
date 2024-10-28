  var roman = '';
  var ones = [
    '',
    'i',
    'ii',
    'iii',
    'iv',
    'v',
    'vi',
    'vii',
    'viii',
    'ix'
  ];
  var tenths = [
    '',
    'x',
    'xx',
    'xxx',
    'xl',
    'l',
    'lx',
    'lxx',
    'lxxx',
    'xc'
  ];
  var hundreds = [
    '',
    'c',
    'cc',
    'ccc',
    'cd',
    'd',
    'dc',
    'dcc',
    'dccc',
    'cm'
  ];

  while (number > 0) {
    if (number >= 1000) {
      roman += 'm';
      number -= 1000;
    } else if (number >= 500) {
      roman += 'd';
      number -= 500;
    } else if (number >= 100) {
      roman += 'c';
      number -= 100;
    } else if (number >= 50) {
      roman += 'l';
      number -= 50;
    } else if (number >= 10) {
      roman += 'x';
      number -= 10;
    } else if (number >= 5) {
      roman += 'v';
      number -= 5;
    } else if (number >= 1) {
      roman += 'i';
      number -= 1;
    }
  }

  return roman;
}



