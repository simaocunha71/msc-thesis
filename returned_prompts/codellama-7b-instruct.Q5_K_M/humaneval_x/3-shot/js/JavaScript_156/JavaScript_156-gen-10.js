  const romanDigits = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i'];
  const romanValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];

  let result = '';
  let num = number;

  for (let i = 0; i < romanDigits.length; i++) {
    while (num >= romanValues[i]) {
      result += romanDigits[i];
      num -= romanValues[i];
    }
  }

  return result;
}



