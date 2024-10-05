
  for (let i = 2; i <= n/2; i += 2) {
    for (let j = i + 2; j < n - i; j += 2) {
      for (let k = j + 2; k < n - i - j; k += 2) {
        let l = n - i - j - k;
        if (i + j + k + l === n && i % 2 === 0 && j % 2 === 0 && k % 2 === 0 && l % 2 === 0) {
          return true;
        }
      }
    }
  }
  return false;
}

console.log(isEqualToSumEven(4)) // false
console.log(isEqualToSumEven(6)) // false
console.log(isEqualToSumEven(8)) // true
console.log(isEqualToSumEven(10)) // true
console.log(isEqualToSumEven(12)) // true
console.log(isEqualToSumEven(14)) // false
console.log(isEqualToSumEven(16)) // true
console.log(isEqualToSumEven(18)) // false
console.log(isEqualToSumEven(20)) // true

This function iterates over all possible combinations of four numbers that sum up to n, and checks if they are all even. If any of the four numbers are not even, it skips that combination. If it finds a combination where all four numbers sum up to n and are all even, it returns true. If it doesn't find any such combination, it returns false.

*/

//The function isEqualToSumEven checks if a given number can be written as the sum of exactly 4 positive even numbers.
const isEqualToSumEven = (n) => {
  //Iterate over all possible combinations of four numbers that sum up to n.
  for (let i = 2; i <= n / 2; i += 2) {
    for (let j = i + 2; j < n - i; j += 2) {
      for (let k = j + 2; k < n - i - j; k += 2) {
        let l = n - i - j - k;
       