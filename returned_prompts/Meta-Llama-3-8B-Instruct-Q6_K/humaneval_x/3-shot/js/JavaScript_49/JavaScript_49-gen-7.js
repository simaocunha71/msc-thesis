  return (Math.pow(10, n)) % p;
} // Not correct
// Corrected:
const modp = (n, p) => {

  if (n < 0) {
    n = (p - 1) % p;
  }
  let result = 1;
  for (let i = 0; i < n; i++) {
    result = (result * 2) % p;
  }
  return result;
} // Corrected answer



