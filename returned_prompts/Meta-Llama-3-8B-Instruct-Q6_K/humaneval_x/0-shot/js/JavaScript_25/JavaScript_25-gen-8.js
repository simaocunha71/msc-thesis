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
      factors.push({ factor: divisor, count });
    }
    divisor++;
  }

  return factors.map((f) => Array(f.count).fill(f.factor));
};
```



Explanation:
The function takes an integer `n` as input and returns a list of prime factors in the order from smallest to largest, each factor listed the number of times it appears in the factorization.

The approach is to start with the smallest prime number, 2, and divide `n` by it as long as it's divisible. This process is repeated until `n` is no longer divisible by 2. The count of divisions is the number of times 2 appears as a factor in the factorization.

Then, the divisor is incremented to the next prime number, and the process is repeated until `n` is reduced to 1. The list of factors is constructed by pushing each factor and its count into the `factors` array.

Finally, the function uses the `map` method to transform the `factors` array into a list of arrays, where each inner array represents the factor repeated the number of times it appears in the factorization.

For example, the factorization of 8 is [2, 2, 2], which is returned as [[2, 2, 2]]. The factorization of 25 is [5, 5], which is returned as [[5, 5]]. The factorization of 70 is [2, 5, 7], which is returned as [[2], [5], [7]].