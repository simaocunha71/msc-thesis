```js
const countDistinctCharacters = (string) => {
  let count = 0;
  let seen = {};

  for (let char of string) {
    let lowerChar = char.toLowerCase();
    if (!seen[lowerChar]) {
      count++;
      seen[lowerChar] = true;
    }
  }

  return count;
}
```