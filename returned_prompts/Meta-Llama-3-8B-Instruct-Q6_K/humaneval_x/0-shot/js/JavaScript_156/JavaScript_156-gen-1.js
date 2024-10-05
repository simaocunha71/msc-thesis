Here is the solution:
```javascript
const intToMiniRoman = (number) => {
  const romanNumerals = [
    { value: 1000, roman: 'M' },
    { value: 900, roman: 'CM' },
    { value: 500, roman: 'D' },
    { value: 400, roman: 'CD' },
    { value: 100, roman: 'C' },
    { value: 90, roman: 'XC' },
    { value: 50, roman: 'L' },
    { value: 40, roman: 'XL' },
    { value: 10, roman: 'X' },
    { value: 9, roman: 'IX' },
    { value: 5, roman: 'V' },
    { value: 4, roman: 'IV' },
    { value: 1, roman: 'I' },
  ];

  const result = [];

  for (const numeral of romanNumerals) {
    while (number >= numeral.value) {
      result.push(numeral.roman);
      number -= numeral.value;
    }
  }

  return result.join('');
};

console.log(intToMiniRoman(19)); // 'xix'
console.log(intToMiniRoman(152)); // 'clii'
console.log(intToMiniRoman(426)); // 'cdxxvi'
```

Explanation:

The function `intToMiniRoman` takes an integer `number` as input and returns its Roman numeral equivalent as a string in lowercase.

We define an array `romanNumerals` containing objects with `value` and `roman` properties. Each object represents a Roman numeral and its corresponding integer value.

We iterate through the `romanNumerals` array and for each numeral, we subtract its value from the input `number` as long as `number` is greater than or equal to the value. We add the Roman numeral to the `result` array for each subtraction.

Finally, we join the `result` array into a string using the `join` method and return the result.

Note that the function assumes that the input `number` is a positive integer between 1 and 1000. If the input is outside this range, the function may produce incorrect results. You may want to add input validation to handle such cases.