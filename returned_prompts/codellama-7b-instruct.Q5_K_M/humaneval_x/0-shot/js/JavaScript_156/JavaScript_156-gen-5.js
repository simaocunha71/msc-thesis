const roman = {
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

  const romanArr = [];
  let num = number;

  while (num > 0) {
    for (let romanDigit in roman) {
      if (num >= roman[romanDigit]) {
        romanArr.push(romanDigit);
        num -= roman[romanDigit];
        break;
      }
    }
  }

  return romanArr.join('');
};

// Testing
const intToMiniRoman = (number) => {
  const roman = {
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

  const romanArr = [];
  let num = number;

  for (const romanDigit in roman) {
    while (num >= roman[romanDigit]) {
      romanArr.push(romanDigit);
      num -= roman[romanDigit];
    }
  }

  return romanArr.join('');
};

// Testing
const intToMiniRoman = (number) => {
  const roman = {
    M: 1000,
    CM: 900,
    D: 500,
    CD: 400,
    C: 100,
    XC: 