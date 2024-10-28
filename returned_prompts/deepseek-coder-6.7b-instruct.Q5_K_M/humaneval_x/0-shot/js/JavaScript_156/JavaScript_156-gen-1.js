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

  let roman = '';

  for (let key in map) {
    while (number >= map[key]) {
      roman += key;
      number -= map[key];
    }
  }

  return roman;
};

console.log(intToMiniRoman(19)); // Output: 'xix'
console.log(intToMiniRoman(152)); // Output: 'clii'
console.log(intToMiniRoman(426)); // Output: 'cdxxvi'


module.exports = intToMiniRoman;

```

## Additional Exercises

1. **Mini Roman to Integer**: Write a function that converts a roman numeral string to its integer equivalent.
2. **Roman Numeral Calculator**: Create a function that takes two roman numerals and an operator (+, -, *, /) as strings and returns the result in roman numeral format.
3. **Valid Roman Numeral**: Write a function that checks if a given string is a valid roman numeral.

## Resources

- [Roman Numerals](https://www.mathsisfun.com/roman-numerals.html)
- [Converting Roman Numerals to Numbers](https://www.rapidtables.com/convert/number/roman-numerals-to-numbers.html)
- [Roman Numerals Calculator](https://www.calculatorsoup.com/calculators/math/roman-numerals-calculator.php)
- [Validating Roman Numerals](https://www.codeproject.com/Articles/108211/Validating-