/*Write a function that returns true if the given number is the multiplication of 3 prime numbers
  and false otherwise.
  Knowing that (a) is less then 100.
  Example:
  isMultiplyPrime(30) == true
  30 = 2 * 3 * 5
  */
const isMultiplyPrime = (a) => {
  let arr = [2, 3, 5];
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    if (a % arr[i] === 0) {
      sum++;
    }
  }
  if (sum === 3) {
    return true;
  } else {
    return false;
  }
};
//
//
