  const romanDigits = [
    ['m', 1000], ['cm', 900], ['d', 500], ['cd', 400],
    ['c', 100], ['xc', 90], ['l', 50], ['xl', 40],
    ['x', 10], ['ix', 9], ['v', 5], ['iv', 4],
    ['i', 1]
  ];

  let result = '';
  for (let i = 0; i < romanDigits.length; i++) {
    while (number >= romanDigits[i][1]) {
      result += romanDigits[i][0];
      number -= romanDigits[i][1];
    }
  }
  return result;
}



