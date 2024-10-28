```javascript
const factorize = (n) => {
  const factors = [];
  let i = 2;
  while (i * i <= n) {
    while (n % i === 0) {
      factors.push(i);
      n /= i;
    }
    i += 1;
  }
  if (n > 1) {
    factors.push(n);
  }
  return factors;
};
```


Explanation:
The function takes an integer `n` as input and returns a list of its prime factors. It iterates from 2 to the square root of `n` and checks if `i` is a factor of `n` by using the modulo operator (`%`). If `i` is a factor, it is added to the list of factors and `n` is divided by `i`. This process continues until `i` is no longer a factor of `n`. If `n` is still greater than 1 after the loop, it means that `n` is a prime number itself, so it is added to the list of factors.

The time complexity of this function is O(√n) because it only needs to iterate up to the square root of `n`. The space complexity is O(1) because it only uses a constant amount of space to store the list of factors and the variables `i` and `n`.