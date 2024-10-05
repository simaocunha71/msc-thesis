```
const modp = (n, p) => {
  let result = 1;
  n = n % p;
  while (n > 0) {
    if (n % 2 === 1) {
      result = (result * n) % p;
    }
    n = Math.floor(n / 2);
  }
  return result;
};
```
This function calculates 2^n modulo p using the exponentiation by squaring algorithm, which is more efficient than repeated multiplication for large values of n. It also reduces the number of operations by taking the modulus of n and p at the beginning, and by only performing the multiplication when n is odd. The result is returned at the end of the function.

Note: The function assumes that p is a prime number. If p is not a prime number, the function may not work correctly. Also, the function does not handle the case where n is negative, and the result may not be correct in that case. If you need to handle negative values of n, you will need to add additional logic to the function.