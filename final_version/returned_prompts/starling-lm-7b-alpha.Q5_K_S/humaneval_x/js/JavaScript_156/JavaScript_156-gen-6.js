  let ones = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix'];
  let tens = ['x', 'xx', 'xx', 'xc', 'l', 'l', 'l', 'xc', 'xl'];
  let hundreds = ['c', 'cc', 'cc', 'cd', 'd', 'd', 'd', 'cd', 'c'];
  let thousands = ['m', 'mm', 'mm', 'mc', 'cm'];

  if (number < 1 || number > 1000) {
    return 'Invalid input';
  }

  return thousands[Math.floor(number / 1000)] + hundreds[(number % 1000) / 100] + tens[(number % 100) / 10] + ones[number % 10];
}



