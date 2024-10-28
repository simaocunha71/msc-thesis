  if(n < 2)
    return false;
  for(let i = 2; i <= Math.sqrt(n); i++)
    if(n % i === 0)
      return false;
  return true;
};

module.exports = isPrime;
```

The function `isPrime` checks if a given number `n` is prime by looping from `2` to the square root of `n` and checking if `n` is divisible by any of these numbers. If `n` is divisible by any number, it is not a prime number, and the function returns `false`. If `n` is not divisible by any number in the range, it is a prime number, and the function returns `true`.

The reason we only need to check up to the square root of `n` is that a larger factor of the number would be a multiple of smaller factor that has already been checked.

Note: In JavaScript, `Math.sqrt(n)` returns the square root of `n`. `n % i` returns the remainder of `n` divided by `i`. The `==` operator in JavaScript checks for value equality, while the `===` operator checks for both value and type equality.



## Problem 2:

```javascript
