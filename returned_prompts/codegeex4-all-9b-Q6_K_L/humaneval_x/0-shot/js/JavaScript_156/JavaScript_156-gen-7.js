```js
const intToMiniRoman = (number) => {
  const lookup = [
    ['i', 1],
    ['iv', 4],
    ['v', 5],
    ['ix', 9],
    ['x', 10],
    ['xl', 40],
    ['l', 50],
    ['xc', 90],
    ['c', 100],
    ['cd', 400],
    ['d', 500],
    ['cm', 900],
    ['m', 1000]
  ];

  let roman = '';
  for (let i = lookup.length - 1; i >= 0; i--) {
    while (number >= lookup[i][1]) {
      number -= lookup[i][1];
      roman += lookup[i][0];
    }
  }
  return roman;
};
```
