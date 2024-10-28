```
const intToMiniRoman = (number) => {
  const romanNumerals = {
    1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
  };

  let result = '';
  Object.keys(romanNumerals).sort((a, b) => b - a).forEach((value) => {
    while (number >= value) {
      result += romanNumerals[value];
      number -= value;
    }
  });

  return result.toLowerCase();
};
```
In this solution, we use an object `romanNumerals` to store the roman numerals and their corresponding integer values. We then iterate through the object's keys in descending order and subtract the value from the number as long as it's greater than or equal to the value. We add the corresponding roman numeral to the result string each time we subtract the value. Finally, we return the result string in lowercase. This approach ensures that the roman numeral is constructed in the correct order and that the number is correctly represented as a roman numeral.