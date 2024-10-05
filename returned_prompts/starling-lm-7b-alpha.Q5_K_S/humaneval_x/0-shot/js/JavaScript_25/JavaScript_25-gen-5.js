To solve this problem, first we need to find all the prime factors of the given integer, and then we need to sort them from smallest to largest. We can achieve this by using a while loop and a for loop.

Here's the step-by-step solution:

1. Initialize an empty array `factors` to store the prime factors of the number.
2. Initialize a variable `i` to 2, the smallest prime number.
3. While `i` is less than or equal to the square root of `n`, do the following:
   a. Check if `n` is divisible by `i` (i.e., if `n % i == 0`).
      i. If it is, then `n` is divisible by `i`, so we found a factor. We add `i` to the `factors` array and update `n` by dividing it by `i`.
      ii. If it's not, then we increment `i` by 1 and continue to the next iteration.
4. After the while loop, check if `n` is still greater than 1. If it is, then it means `n` itself is a prime factor and should be added to the `factors` array.
5. Finally, sort the `factors` array in ascending order using the `sort` function and return it.

Here's the code implementation of the above steps:

```javascript
const factorize = (n) => {
  let factors = [];
  let i = 2;

  while (i * i <= n) {
    if (n % i === 0) {
      factors.push(i);
      n /= i;
    } else {
      i++;
    }
  }

  if (n > 1) {
    factors.push(n);
  }

  return factors.sort((a, b) => a - b);
};
```

Now you can test the function with different values:

```javascript
console.log(factorize(8));    // [2, 2, 2]
console.log(factorize(25));   // [5, 5]
console.log(factorize(70));   // [