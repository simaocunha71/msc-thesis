
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
  let result = '';
  for (let key in roman) {
    while (number >= +key) {
      result += key;
      number -= +key;
    }
  }
  return result;
};

intToMiniRoman(19); // 'xix'
intToMiniRoman(152); // 'clii'
intToMiniRoman(426); // 'cdxxvi'


/*
Given a positive integer, obtain its roman numeral equivalent as a string,
and return it in lowercase.
Restrictions: 1 <= num <= 1000

Examples:
>>> intToMiniRoman(19) == 'xix'
>>> intToMiniRoman(152) == 'clii'
>>> intToMiniRoman(426) == 'cdxxvi'
*/

*/


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
  let result = '';
  for (let key in roman) {
    while (number >= +key) {
      result += key;
      number -= +key;
    }
  }
  return result;
