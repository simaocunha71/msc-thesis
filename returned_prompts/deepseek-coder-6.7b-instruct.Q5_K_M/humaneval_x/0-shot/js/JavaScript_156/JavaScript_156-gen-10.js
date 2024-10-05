  const mapping = {
      1: 'i',
      4: 'iv',
      5: 'v',
      9: 'ix',
      10: 'x',
      40: 'xl',
      50: 'l',
      90: 'xc',
      100: 'c',
      400: 'cd',
      500: 'd',
      900: 'cm',
      1000: 'm'
  };

  let result = '';

  for (let key of Object.keys(mapping).sort((a, b) => b - a)) {
      while (number >= key) {
          number -= key;
          result += mapping[key];
      }
  }

  return result;
};

console.log(intToMiniRoman(19)); // 'xix'
console.log(intToMiniRoman(152)); // 'clii'
console.log(intToMiniRoman(426)); // 'cdxxvi'
```

This function works by mapping the integers to their corresponding roman numeral equivalents in a dictionary. It then loops over the keys of the dictionary, in descending order, and as long as the number being converted is greater than or equal to the current key, it subtracts the key from the number and appends the corresponding roman numeral to the result.

The function finally returns the result, which is the roman numeral equivalent of the input number.

Please note that this function doesn't handle numbers greater than 1000 because the problem statement specifies that the input number will be less than or equal to 1000.
*/

function intToMiniRoman(number) {
    const mapping = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        100