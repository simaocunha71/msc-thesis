/*Write a function that returns true if the given number is the multiplication of 3 prime numbers
  and false otherwise.
  Knowing that (a) is less then 100.
  Example:
  isMultiplyPrime(30) == true
  30 = 2 * 3 * 5
  */
const isMultiplyPrime = (a) => {
  if ((a % 2 === 0 || a % 3 === 0) && (a > 1)) return false;
  // if the given number ends with '0' or '-1', then it is not prime, so we return false.
  else return true;
};

console.log(isMultiplyPrime(10)); //true;
console.log(isMultiplyPrime(35)); //false;
