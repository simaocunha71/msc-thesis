```js
const makeAPile = (n) => {
  const result = [];
  let currentLevel = n;
  while (currentLevel > 0) {
    result.push(currentLevel);
    currentLevel += (currentLevel % 2 === 0 ? 2 : 1);
  }
  return result;
};
```
