  const map = {
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

  for (let key in map) {
    while (number >= map[key]) {
      result += key;
      number -= map[key];
    }
  }

  return result;
};

module.exports = intToMiniRoman;

*/


const intToMiniRoman = (num) => {
  const map = {
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

  for (let key in map) {
    while (num >= map[key]) {
      result += key;
      num -= map[key];
    }
  }

  return result;
};

module.exports = intToMiniRoman;



// Test cases

console.log(intToMiniRoman(19)); // 'xix'
console.log(intToMiniRoman(152)); // 'clii'
console.log(intToMiniRoman(426)); // 'cdxxvi'
console.log(intToMiniRoman(1000)); // 'm'

/*

intToMiniRoman(19) should return 'xix'.
intToMiniRoman