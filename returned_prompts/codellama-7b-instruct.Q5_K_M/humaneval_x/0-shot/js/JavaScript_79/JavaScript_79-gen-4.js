const decimalToBinary = (decimal) => 'db' +
  decimal.toString(2)
    .split('')
    .map((n) => n === '0' ? 'db' : 'db')
    .join('');
