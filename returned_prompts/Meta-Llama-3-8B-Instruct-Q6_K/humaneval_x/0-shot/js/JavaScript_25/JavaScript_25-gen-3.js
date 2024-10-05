```javascript
const factorize = (n) => {
  const factors = [];
  let divisor = 2;
  while (n > 1) {
    let count = 0;
    while (n % divisor === 0) {
      n /= divisor;
      count++;
    }
    if (count > 0) {
      factors.push({ value: divisor, count });
    }
    divisor++;
  }
  return factors.map((factor) => Array(factor.count).fill(factor.value));
};

// Test cases
console.log(factorize(8)); // [2, 2, 2]
console.log(factorize(25)); // [5, 5]
console.log(factorize(70)); // [2, 5, 7]
```
In this solution, we use a while loop to iterate from 2 to `n` and find the factors of `n`. We keep dividing `n` by the current divisor as long as it is divisible, and increment a counter for each successful division. If the counter is greater than 0, we add the divisor and its count to the `factors` array. Finally, we map the `factors` array to an array of arrays, where each inner array represents the repeated factors. The `fill` method is used to create the repeated factors.