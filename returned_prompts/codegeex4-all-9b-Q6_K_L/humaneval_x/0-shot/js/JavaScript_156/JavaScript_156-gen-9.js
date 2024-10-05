```js
const intToMiniRoman = (number) => {
  let roman = '';
  const map = [[1000, 'm'], [900, 'cm'], [500, 'd'], [400, 'cd'], [100, 'c'], [90, 'xc'], [50, 'l'], [40, 'xl'], [10, 'x'], [9, 'ix'], [5, 'v'], [4, 'iv'], [1, 'i']];
  for (let i = 0; i < map.length; i++) {
    while (number >= map[i][0]) {
      roman += map[i][1];
      number -= map[i][0];
    }
  }
  return roman;
}
```