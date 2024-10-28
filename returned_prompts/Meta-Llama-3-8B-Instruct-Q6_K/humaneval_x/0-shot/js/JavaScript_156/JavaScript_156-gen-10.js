```
const romanNumerals = [
  { value: 1000, roman: 'm' },
  { value: 900, roman: 'cm' },
  { value: 500, roman: 'd' },
  { value: 400, roman: 'cd' },
  { value: 100, roman: 'c' },
  { value: 90, roman: 'xc' },
  { value: 50, roman: 'l' },
  { value: 40, roman: 'xl' },
  { value: 10, roman: 'x' },
  { value: 9, roman: 'ix' },
  { value: 5, roman: 'v' },
  { value: 4, roman: 'iv' },
  { value: 1, roman: 'i' },
];

const intToMiniRoman = (number) => {
  let roman = '';
  for (const numeral of romanNumerals) {
    while (number >= numeral.value) {
      roman += numeral.roman;
      number -= numeral.value;
    }
  }
  return roman.toLowerCase();
};
```


Explanation:
This function iterates through an array of objects representing the roman numerals and their corresponding values. It uses a while loop to repeatedly subtract the largest possible roman numeral value from the input number and add the corresponding roman numeral to the result string, until the number is reduced to zero. The result is the roman numeral equivalent of the input number as a string, in lowercase. The function returns this string.