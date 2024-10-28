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

const result = Object.keys(roman)
  .map(key => {
    const value = roman[key];
    while (number >= value) {
      result.push(key);
      number -= value;
    }
  })
  .join('');

return result;

};

// Tests
console.log(intToMiniRoman(19) === 'xix'); // True
console.log(intToMiniRoman(152) === 'clii'); // True
console.log(intToMiniRoman(426) === 'cdxxvi'); // True





























































































































































































































































