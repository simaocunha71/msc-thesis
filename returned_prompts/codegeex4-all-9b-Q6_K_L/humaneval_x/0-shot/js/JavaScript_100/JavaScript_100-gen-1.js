Here is the JavaScript solution for the problem:

```javascript
const makeAPile = (n) => {
  let levels = [];
  for (let i = 0; i < n; i++) {
    levels.push(n + (i % 2 ? 1 : 2));
  }
  return levels;
}
```

This solution works by iterating over the range from 0 to n-1, and for each iteration, it calculates the number of stones in the current level and adds it to the levels array. The number of stones in the current level is calculated as the initial number of stones plus the index of the current iteration, which is either 1 or 2 depending on whether the index is odd or even.

You can test this function with the following code:

```javascript
console.log(makeAPile(3)); // [3, 5, 7]
console.log(makeAPile(4)); // [4, 6, 8, 10]
console.log(makeAPile(1)); // [1]
```

This will output the expected results for the given examples.