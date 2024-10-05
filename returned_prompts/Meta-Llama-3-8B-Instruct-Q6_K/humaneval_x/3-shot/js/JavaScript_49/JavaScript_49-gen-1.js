  return (Math.pow(10, n) % p);
} // This is not correct solution. Modulo operation should be applied after exponentiation, not before. We should use exponentiation by squaring algorithm
// Correct solution:
const modp = (n, p) => {
  let result = 1;
  let base = 2;
  while (n > 0) {
    if (n % 2 == 1) {
      result = (result * base) % p;
    }
    base = (base * base) % p;
    n = Math.floor(n / 2);
  }
  return result;
} // This function calculates (2^n) % p, which is the correct solution. It uses exponentiation by squaring algorithm. The time complexity is O(log n).