This problem is asking to create a function `modp` that takes two arguments, `n` and `p`, and returns the value of `2^n` modulo `p`.

Here is the solution:
```
const modp = (n, p) => {
  if (n === 0) return 1;
  let result = 1;
  let x = 2;
  while (n > 0) {
    if (n % 2 === 1) {
      result = (result * x) % p;
    }
    x = (x * x) % p;
    n = Math.floor(n / 2);
  }
  return result;
};
```
This function uses the property of modular exponentiation that `a^(b*c) ≡ (a^b)^c (mod p)`. It also uses the fact that `2^(2^k) ≡ (2^2)^(2^(k-1)) (mod p)`.

The function works by repeatedly squaring `x` and multiplying `result` by `x` if `n` is odd. It also reduces `n` by half in each iteration. When `n` becomes zero, the function returns the final value of `result`.

The function also handles the case where `n` is zero by returning 1, which is the identity element for modular exponentiation.

You can test the function with the examples you provided:
```
console.log(modp(3, 5)); // 3
console.log(modp(1101, 101)); // 2
console.log(modp(0, 101)); // 1
console.log(modp(3, 11)); // 8
console.log(modp(100, 101)); // 1
```
I hope this helps! Let me know if you have any questions.