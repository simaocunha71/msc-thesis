Here is the solution to the problem:

```javascript
const factorize = (n) => {
  let factors = [];
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
  return factors.map((factor) => factor.value).sort((a, b) => a - b);
};
```

In this solution, we use a while loop to iterate through all numbers from 2 to `n`. For each number `divisor`, we check if it is a factor of `n` by using the modulo operator `%`. If it is a factor, we divide `n` by `divisor` and increment a counter `count`. We continue dividing `n` by `divisor` as long as it is a factor. Once we are done dividing `n` by `divisor`, we add the factor `divisor` to our list of factors with its corresponding count.

Finally, we use the `map` method to extract the values from our list of factors and the `sort` method to sort them in ascending order. The resulting list of prime factors is then returned.