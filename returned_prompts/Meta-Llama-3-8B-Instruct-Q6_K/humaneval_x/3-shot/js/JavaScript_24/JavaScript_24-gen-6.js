  for (let i = n - 1; i > 0; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return 1;
}
// or
const largestDivisor = (n) => {
  for (let i = Math.floor(Math.sqrt(n)); i > 1; i--) {
    if (n % i === 0) {
      return n / i;
    }
  }
  return 1;
}
// or
const largestDivisor = (n) => {
  for (let i = Math.floor(Math.sqrt(n)); i > 1; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return n;
}