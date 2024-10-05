/*Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
  Example
  isEqualToSumEven(4) == false
  isEqualToSumEven(6) == false
  isEqualToSumEven(8) == true
  */
const isEqualToSumEven = (n) => {
  let count = 0;
  for (let i = 2; i <= n; i += 2) {
    count++;
    if (count === 4) return true;
  }
  return false;
}


