```javascript
const intToMiniRoman = (number) => {
  let roman = '';
  const values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  const symbols = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i'];

  for (let i = 0; i < values.length; i++) {
    while (number >= values[i]) {
      number -= values[i];
      roman += symbols[i];
    }
  }

  return roman;
}
```