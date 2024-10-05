```
const makeAPile = (n) => {
  const result = [];
  let currentLevel = n;
  let current = n;

  while (currentLevel > 0) {
    result.unshift(current);
    currentLevel--;

    if (current % 2 === 0) {
      current += 1;
    } else {
      current += 2;
    }
  }

  return result;
};

console.log(makeAPile(3)); // [3, 5, 7]
``` 