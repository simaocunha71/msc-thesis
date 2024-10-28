  const romanNumeral = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix'];
  const tens = ['', 'x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc'];
  const hundreds = ['', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dcc', 'cm'];
  const thousands = ['', 'm', 'mm', 'mmm'];

  let result = '';
  let n = number;

  while (n >= 1000) {
    result += thousands[n / 1000];
    n = n % 1000;
  }

  while (n >= 100) {
    result += hundreds[n / 100];
    n = n % 100;
  }

  while (n >= 10) {
    result += tens[n / 10];
    n = n % 10;
  }

  while (n >= 1) {
    result += romanNumeral[n];
    n = n % 1;
  }

  return result;
}