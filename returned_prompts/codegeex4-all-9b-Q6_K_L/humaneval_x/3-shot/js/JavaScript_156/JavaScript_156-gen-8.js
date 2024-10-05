  const ones = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix'];
  const tens = ['x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc'];
  const hundreds = ['c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dcc', 'cm'];
  const thousands = ['m', 'mm', 'mmm'];

  let result = '';
  let thousands_count = Math.floor(number / 1000);
  let hundreds_count = Math.floor((number % 1000) / 100);
  let tens_count = Math.floor((number % 100) / 10);
  let ones_count = number % 10;

  for (let i = 0; i < thousands_count; i++) {
    result += thousands[0];
  }

  for (let i = 0; i < hundreds_count; i++) {
    result += hundreds[0];
  }

  for (let i = 0; i < tens_count; i++) {
    result += tens[0];
  }

  for (let i = 0; i < ones_count; i++) {
    result += ones[0];
  }

  return result;
}