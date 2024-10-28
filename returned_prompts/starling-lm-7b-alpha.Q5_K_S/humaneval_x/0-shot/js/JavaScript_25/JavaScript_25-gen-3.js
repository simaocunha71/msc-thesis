One way to solve this Kata is to use a loop to check each number from 2 to n and divide n by that number as long as it's possible. This way, we get all the prime factors with their counts.

Here's one possible implementation:

```javascript
function factorize(n) {
    var factors = [];
    var count = 2;

    while (n > 1) {
        while (n % count === 0) {
            factors.push(count);
            n /= count;
        }
        count++;
    }
    return factors;
}
```

This implementation works by initializing an empty array `factors` to store the factors, and a variable `count` to start from 2. Inside the `while` loop, we check if `n` is divisible by `count` using the modulo operator `%`. If it is, we add `count` to `factors` and divide `n` by `count`. We then increment `count` and repeat the process until `n` becomes 1.

Finally, we return the `factors` array, which will contain all the prime factors of the input number in ascending order.

For example, if we call `factorize(8)`, the function will return `[2, 2, 2]`, because 8 can be factored as 2 * 2 * 2.

Similarly, if we call `factorize(25)`, the function will return `[5, 5]`, because 25 can be factored as 5 * 5.

And if we call `factorize(70)`, the function will return `[2, 5, 7]`, because 70 can be factored as 2 * 5 * 7.

Note that this implementation assumes that the input number `n` is a positive integer greater than 1. If `n` is less than or equal to 1, the function will not work correctly.
```







/*
  Return list of prime factors of given integer in the order from smallest to largest.
  Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
  Input number should