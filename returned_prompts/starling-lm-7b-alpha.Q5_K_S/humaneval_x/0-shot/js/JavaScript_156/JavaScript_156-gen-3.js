
  const romanNumerals = {
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

  for (let numeral in romanNumerals) {
    while (number >= romanNumerals[numeral]) {
      result += numeral;
      number -= romanNumerals[numeral];
    }
  }

  return result;
};

intToMiniRoman(426); // "cdxxvi"

/*
  Correct Solution:

  const intToMiniRoman = (number) => {

  const romanNumerals = {
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

  for (let numeral in romanNumerals) {
    while (number >= romanNumerals[numeral]) {
      result += numeral;
      number -= romanNumerals[numeral];
    }
  }

  return result;
};

intToMiniRoman(426); // "cdxxvi"


Explanation:

  Given a positive integer, obtain its roman numeral equivalent as a string,
  and return it in lowercase.

  Restrictions: 1 <= num <= 1000

  Examples:
  >>> intToMiniRoman(19) ==