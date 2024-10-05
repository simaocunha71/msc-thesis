You can create a function to convert an integer to a roman numeral by mapping each integer to its corresponding roman numeral and then iterating through the integer, subtracting the mapped integer from the total integer and appending the corresponding roman numeral to a string until the integer is 0. Here's how you can implement this:

```javascript
const intToMiniRoman = (number) => {
  let roman = '';
  let romanNumeralMap = [
    { num: 1000, roman: 'm' },
    { num: 900, roman: 'cm' },
    { num: 500, roman: 'd' },
    { num: 400, roman: 'cd' },
    { num: 100, roman: 'c' },
    { num: 90, roman: 'xc' },
    { num: 50, roman: 'l' },
    { num: 40, roman: 'xl' },
    { num: 10, roman: 'x' },
    { num: 9, roman: 'ix' },
    { num: 5, roman: 'v' },
    { num: 4, roman: 'iv' },
    { num: 1, roman: 'i' },
  ];

  for (let i = 0; i < romanNumeralMap.length; i++) {
    while (number >= romanNumeralMap[i].num) {
      roman += romanNumeralMap[i].roman;
      number -= romanNumeralMap[i].num;
    }
  }

  return roman;
}
```

You can now test the function with the given examples:

```javascript
console.log(intToMiniRoman(19)); // Output: 'xix'
console.log(intToMiniRoman(152)); // Output: 'clii'
console.log(intToMiniRoman(426)); // Output: 'cdxxvi'
```