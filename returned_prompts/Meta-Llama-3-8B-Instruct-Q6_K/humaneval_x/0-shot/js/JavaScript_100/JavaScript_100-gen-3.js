Here is the solution in JavaScript:

```javascript
const makeAPile = (n) => {
  const result = [];
  let level = n;
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      level += 1;
    } else {
      level += 2;
    }
    result.push(level);
  }
  return result;
};
```

This function uses a for loop to iterate from 1 to n. Inside the loop, it checks if the current level number is even or odd. If it's even, it adds 1 to the level number. If it's odd, it adds 2. The updated level number is then pushed to the result array. The result array is returned at the end of the function.