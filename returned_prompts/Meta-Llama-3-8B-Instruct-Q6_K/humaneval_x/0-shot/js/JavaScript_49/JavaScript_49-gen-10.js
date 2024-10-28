```
const modp = (n, p) => {
  let result = 1;
  while (n > 0) {
    if (n % 2 === 1) {
      result = (result * p) % p;
    }
    n = Math.floor(n / 2);
    p = (p * p) % p;
  }
  return result;
};
```


This function calculates 2^n modulo p using the property of modular exponentiation, which is (a * b) % p = ((a % p) * (b % p)) % p. It iterates over the bits of the exponent n, multiplying the result by p if the bit is 1, and squaring p if the bit is 0. This way, it efficiently calculates 2^n modulo p without having to calculate the full value of 2^n.

The function also handles the case where n is 0, in which case the result is 1. This is because 2^0 is defined to be 1.