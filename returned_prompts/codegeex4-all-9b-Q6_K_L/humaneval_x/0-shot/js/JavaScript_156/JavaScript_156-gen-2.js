To convert an integer to its Roman numeral equivalent, we need to understand the Roman numeral system. The system uses combinations of letters from the Latin alphabet (I, V, X, L, C, D, M) to represent numbers. The key rules for converting an integer to Roman numerals are:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given these rules, we can create a function that maps the integer to the corresponding Roman numeral. We'll start from the largest value (1000) and work our way down to the smallest (1), appending the Roman numeral representation to a string until the entire number is converted.

Here's how you can implement the `intToMiniRoman` function:

```javascript
const intToMiniRoman = (number) => {
  // Define the Roman numeral mappings for each place value
  const romanNumerals = [
    [1000, 'm'],
    [900, 'cm'],
    [500, 'd'],
    [400, 'cd'],
    [100, 'c'],
    [90, 'xc'],
    [50, 'l'],
    [40, 'xl'],
    [10, 'x'],
    [9, 'ix'],
    [5, 'v'],
    [4, 'iv'],
    [1, 'i']
  ];

  // Initialize the result string
  let result = '';

  // Loop through the Roman numeral mappings
  for (const [value, numeral] of romanNumerals) {
    // Append the Roman numeral to the result as many times as the number can be divided by the value
    while (number >= value) {
      result += numeral;
      number -= value;
    }
  }

  // Return the result string
  return result;
};
```

Let's test the function with the provided examples:

```javascript
console.log(intToMiniRoman(19)); // Should print 'xix'
console.log(intToMiniRoman(152)); // Should print 'clii'
console.log(intToMiniRoman(426)); // Should print 'cdxxvi'
```

The function should correctly convert the given integers to their Roman numeral equivalents.