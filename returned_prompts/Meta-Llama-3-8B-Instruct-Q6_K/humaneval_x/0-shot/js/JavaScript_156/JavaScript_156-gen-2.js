```
const intToMiniRoman = (number) => {
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

  let roman = '';
  for (const numeral of romanNumerals) {
    while (number >= numeral.value) {
      roman += numeral.numeral;
      number -= numeral.value;
    }
  }
  return roman.toLowerCase();
};
```


Explanation:
The provided function `intToMiniRoman` takes a positive integer as an input and returns its roman numeral equivalent as a string in lowercase. The function works by iterating through a list of roman numerals in descending order of their values. For each numeral, it subtracts the numeral's value from the input number as many times as possible, appending the numeral's string to the result each time. Finally, it returns the result as a lowercase string.