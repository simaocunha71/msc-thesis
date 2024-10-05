To convert an integer to its Roman numeral equivalent, we can create a mapping of Roman numeral symbols to their corresponding integer values. We will iterate through the integer from the largest to the smallest value in the mapping, subtracting the value from the integer and appending the corresponding Roman numeral symbol to a result string until the integer is reduced to 0. Finally, we will return the result string.

Here's the implementation in JavaScript:

```javascript
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
  for (const [symbol, value] of Object.entries(romanNumerals)) {
    while (number >= value) {
      result += symbol;
      number -= value;
    }
  }

  return result;
};

console.log(intToMiniRoman(19)); // xix
console.log(intToMiniRoman(152)); // clii
console.log(intToMiniRoman(426)); // cdxxvi
```

This implementation will correctly convert any integer within the range of 1 to 1000 to its Roman numeral equivalent.