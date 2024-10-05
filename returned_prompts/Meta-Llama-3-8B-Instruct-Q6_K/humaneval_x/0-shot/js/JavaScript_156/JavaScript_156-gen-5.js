```
const romanNumerals = [
  { value: 1000, numeral: 'm' },
  { value: 900, numeral: 'cm' },
  { value: 500, numeral: 'd' },
  { value: 400, numeral: 'cd' },
  { value: 100, numeral: 'c' },
  { value: 90, numeral: 'xc' },
  { value: 50, numeral: 'l' },
  { value: 40, numeral: 'xl' },
  { value: 10, numeral: 'x' },
  { value: 9, numeral: 'ix' },
  { value: 5, numeral: 'v' },
  { value: 4, numeral: 'iv' },
  { value: 1, numeral: 'i' },
];

const intToMiniRoman = (number) => {
  let result = '';

  for (const numeral of romanNumerals) {
    while (number >= numeral.value) {
      result += numeral.numeral;
      number -= numeral.value;
    }
  }

  return result.toLowerCase();
};

console.log(intToMiniRoman(19)); // 'xix'
console.log(intToMiniRoman(152)); // 'clii'
console.log(intToMiniRoman(426)); // 'cdxxvi'
```