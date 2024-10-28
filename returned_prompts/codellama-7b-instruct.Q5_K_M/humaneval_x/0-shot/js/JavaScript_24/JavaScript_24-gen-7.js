/* For a given number n, find the largest number that divides n evenly, smaller than n
  >>> largestDivisor(15)
  5
  */
const largestDivisor = (n) => {

  let largest = 0;
  for (let i = 1; i < n; i++) {
    if (n % i === 0) {
      largest = i;
    }
  }
  return largest;
}
