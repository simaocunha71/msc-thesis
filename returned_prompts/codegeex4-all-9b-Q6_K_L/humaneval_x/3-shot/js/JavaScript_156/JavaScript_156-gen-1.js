  let roman = '';
  let romanNumeral = [
    ['i', 1],
    ['x', 10],
    ['c', 100],
    ['m', 1000],
  ];

  for (let i = romanNumeral.length - 1; i >= 0; i--) {
    while (number >= romanNumeral[i][1]) {
      roman += romanNumeral[i][0];
      number -= romanNumeral[i][1];
    }
  }

  return roman.toLowerCase();
}



