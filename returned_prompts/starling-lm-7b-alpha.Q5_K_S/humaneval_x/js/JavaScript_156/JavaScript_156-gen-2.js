  if (number < 1 || number > 1000) {
    return undefined;
  }

  const numerals = {
    M: 1000,
    CM: 900,
    D: 500,
    CD: 400,
    C: 100,
    XC: 90,
    L: 50,
    XL: 40,
    X: 10,
    IX: 9,
    V: 5,
    IV: 4,
    I: 1
  };

  let result = '';

  for (const [roman, value] of Object.entries(numerals)) {
    while (number >= value) {
      result += roman;
      number -= value;
    }
  }

  return result;
}


