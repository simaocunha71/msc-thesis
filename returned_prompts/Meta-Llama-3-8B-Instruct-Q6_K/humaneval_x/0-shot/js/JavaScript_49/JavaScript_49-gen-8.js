```
const modp = (n, p) => {
  if (n === 0) return 1;
  let result = 1;
  let power = n;
  while (power > 0) {
    if (power % 2 === 1) {
      result = (result * result) % p;
    }
    power = Math.floor(power / 2);
  }
  return result;
};
```


Explanation:
The function `modp(n, p)` calculates 2^n modulo p using the property of exponentiation modulo p.

The base case is when `n` is 0, in which case the function returns 1, as 2^0 is 1.

For the recursive case, the function uses a while loop to repeatedly square the result (initially 1) and update the power of 2 by dividing it by 2. If the power is odd, the result is updated by multiplying it with the current result.

The loop continues until the power becomes 0. At this point, the result is the value of 2^n modulo p.

The function uses the modulo operator `%` to ensure that the result remains within the range [0, p-1]. This is necessary to avoid overflowing the result and to ensure that the function works correctly for large values of `n` and `p`.