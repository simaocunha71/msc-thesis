/* For a given number n, find the largest number that divides n evenly, smaller than n
  >>> largestDivisor(15)
  5
  */
const largestDivisor = (n) => {
  for (let i = n; i > 1; i--) {
    if (n % i === 0) return i;
  }
  return 1;
}
