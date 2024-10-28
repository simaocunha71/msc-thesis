To convert an integer to its Roman numeral equivalent, we can use a lookup table to map each Roman numeral to its corresponding integer value. We can then iterate through the number, subtracting the largest possible Roman numeral value until the number is reduced to zero.

Here's the implementation for the `intToMiniRoman` function:
```javascript
const intToMiniRoman = (number) => {
  const romanNumeralMap = [
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
  let romanNumeral = '';
  for (let [integer, numeral] of romanNumeralMap) {
    while (number >= integer) {
      romanNumeral += numeral;
      number -= integer;
    }
  }
  return romanNumeral;
};
```

We can test the function with the provided examples:
```javascript
console.log(intToMiniRoman(19)); // Output: xix
console.log(intToMiniRoman(152)); // Output: clii
console.log(intToMiniRoman(426)); // Output: cdxxvi
```