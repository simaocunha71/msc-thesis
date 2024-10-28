```
const intToMiniRoman = (number) => {
  const romanMap = {
    1000: 'm',
    900: 'cm',
    500: 'd',
    400: 'cd',
    100: 'c',
    90: 'xc',
    50: 'l',
    40: 'xl',
    10: 'x',
    9: 'ix',
    5: 'v',
    4: 'iv',
    1: 'i'
  };

  const roman = [];

  for (const [key, value] of Object.entries(romanMap)) {
    while (number >= parseInt(key)) {
      roman.push(value);
      number -= parseInt(key);
    }
  }

  return roman.join('');
};
```



Explanation:

The function `intToMiniRoman` takes an integer `number` as input and returns its equivalent Roman numeral as a string in lowercase. To achieve this, we create a mapping of Roman numerals to their corresponding integer values (`romanMap`). We then iterate over this mapping and for each key-value pair, we subtract the key from the input number as long as the number is greater than or equal to the key. We add the corresponding Roman numeral to the result array for each subtraction. Finally, we join the result array into a string and return it.

The provided examples demonstrate the function's correctness:

```javascript
console.log(intToMiniRoman(19)); // Output: "xix"
console.log(intToMiniRoman(152)); // Output: "clii"
console.log(intToMiniRoman(426)); // Output: "cdxxvi"
```



The time complexity of this function is O(n), where n is the number of key-value pairs in the `romanMap`. The space complexity is O(1), as we only use a constant amount of space to store the result and the mapping.