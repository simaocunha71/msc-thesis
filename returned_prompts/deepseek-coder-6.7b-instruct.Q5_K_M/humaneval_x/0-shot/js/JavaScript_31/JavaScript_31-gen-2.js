  if (n < 2) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
};

```

### Explanation

This function `isPrime` checks if a given number `n` is a prime number. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Therefore, this function starts by checking if `n` is less than 2 (the smallest prime number), and if it is, it returns `false`.

Then, it uses a for loop to check if `n` has any divisors other than 1 and itself. The loop starts from 2 (the smallest prime number) and goes up to the square root of `n`, because a larger factor of `n` must be a multiple of a smaller factor that has already been checked.

Inside the loop, it uses the modulo operator (`%`) to check if `n` is divisible by `i`. If it is, the function returns `false`, because `n` is not a prime number.

If the loop completes without finding any divisors other than 1 and `n`, the function returns `true`, because `n` is a prime number.

### Testing

You can test this function using any JavaScript testing framework such as Jest or Mocha. Here is a simple example using Jest:

```javascript
test('isPrime function', () => {
  expect(isPrime(6)).toBe(false);
  expect(isPrime(101)).toBe(true);
  expect(isPrime(11)).toBe(true);
  expect(isPrime(13441)).toBe(true);
  expect(isPrime(61)).toBe(true);
  expect(isPrime(4)).toBe(false);
  expect(isPrime(1)).toBe(false);
});
```

This test suite checks the `isPrime` function with several different test cases, and checks that the function returns the expected results.

To run the test