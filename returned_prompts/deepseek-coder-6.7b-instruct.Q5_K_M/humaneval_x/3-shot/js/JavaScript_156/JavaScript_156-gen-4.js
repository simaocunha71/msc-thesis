  const map = [[1000, 'm'], [900, 'cm'], [500, 'd'], [400, 'cd'], 
               [100, 'c'], [90, 'xc'], [50, 'l'], [40, 'xl'], 
               [10, 'x'], [9, 'ix'], [5, 'v'], [4, 'iv'], [1, 'i']];
  let result = '';

  for (const [value, numeral] of map) {
    while (number >= value) {
      result += numeral;
      number -= value;
    }
  }

  return result;
}



