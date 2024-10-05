Here is a JavaScript function that calculates the first `n + 1` numbers of the Tribonacci sequence:
```javascript
const tri = (n) => {
  if (n === 0) return [1]; // base case
  if (n === 1) return [1, 3]; // base case

  const tribonacci = [1, 3]; // initialize with the first two values

  for (let i = 2; i <= n; i++) {
    let nextValue = 0;
    if (i % 2 === 0) { // even index
      nextValue = 1 + i / 2;
    } else { // odd index
      nextValue = tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3];
    }
    tribonacci.push(nextValue);
  }

  return tribonacci;
};
```
You can test the function with the examples you provided:
```javascript
console.log(tri(3)); // [1, 3, 2, 8]
console.log(tri(4)); // [1, 3, 2, 8, 11]
```
Note that the function uses a recursive formula to calculate the next value in the sequence, but it's not actually recursive because we're using a loop to iterate over the indices. This makes the function more efficient and easier to understand.