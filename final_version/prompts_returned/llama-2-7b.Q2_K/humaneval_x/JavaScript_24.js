/* For a given number n, find the largest number that divides n evenly, smaller than n
  >>> largestDivisor(15)
  5
  */
const largestDivisor = (n) => {
  let currentMax = 0;
  for (let i of [...Array(n).keys()]) {
    // console.log(`>>> test ${i}`);
    if ((i % n === 0 && currentMax < i)) {
      currentMax = i;
    } else if ((i % n !== 0 || !(currentMax >= Math.floor(n / 2))) && (i % n) < Math.max(...Array(n).keys().map((j) => largestDivisor(Math.ceil(n / j))), 1)) {
      currentMax = i;
    }
    // console.log(`>>> test ${i}`);
  }
  return currentMax || -1;
};
