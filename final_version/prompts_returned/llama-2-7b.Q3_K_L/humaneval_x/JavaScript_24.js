/* For a given number n, find the largest number that divides n evenly, smaller than n
  >>> largestDivisor(15)
  5
  */
const largestDivisor = (n) => {
  let current = 2;
  while (current * current < n) {
    if (n % current === 0 && current > 1 && current < n / 3) return current;
    current += 1;
  }
};

module.exports = largestDivisor;
