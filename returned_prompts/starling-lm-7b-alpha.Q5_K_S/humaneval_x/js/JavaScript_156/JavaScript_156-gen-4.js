  const m = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
  const v = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];

  let result = "";
  for (let i = 0; i < v.length; i++) {
    while (number >= v[i]) {
      result += m[i];
      number -= v[i];
    }
  }

  return result;
}



