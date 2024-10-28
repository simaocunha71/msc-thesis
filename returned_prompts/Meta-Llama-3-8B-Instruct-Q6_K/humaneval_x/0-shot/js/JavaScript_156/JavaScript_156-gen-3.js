```
const romanNumerals = {
  1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
};

const intToMiniRoman = (number) => {
  let roman = '';
  for (let i = 1000; i >= 1; i /= 10) {
    while (number >= i) {
      roman += romanNumerals[i];
      number -= i;
    }
  }
  return roman.toLowerCase();
};
```


Explanation:
- We create an object `romanNumerals` that maps integer values to their roman numeral equivalents.
- The function `intToMiniRoman` takes an integer `number` as input.
- We initialize an empty string `roman` to store the roman numeral representation of the input number.
- We loop through the powers of 10 from 1000 to 1 (inclusive), and for each power, we subtract the power from the input number as many times as possible (using the `while` loop).
- For each subtraction, we add the corresponding roman numeral to the `roman` string.
- Finally, we return the `roman` string in lowercase using the `toLowerCase()` method.

This solution works because the roman numeral system is based on subtractive notation, where a smaller numeral is subtracted from a larger one to represent a smaller value. By looping through the powers of 10 and subtracting the largest possible value at each step, we can build the roman numeral representation of the input number.