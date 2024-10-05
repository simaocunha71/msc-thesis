  let isPrime = (b) => {
    let i = 2;
    while (i < b) {
      if (b % i === 0) {
        return false;
      }
      i++;
    }
    return true;
  };

  if (a < 3) {
    return false;
  }

  while (a > 1) {
    if (!isPrime(a)) {
      return false;
    }
    a = a / 3;
  }
  return true;
};

console.log(isMultiplyPrime(30));




/* Write a function that counts the number of vowels in a given string.
The function should return the number of vowels found in the string.
  Example:
  countVowels("Hello World") == 3
  */

const countVowels = (str) => {
  let vowels = 'aeiouAEIOU';
  let counter = 0;
  for (let letter of str) {
    if (vowels.includes(letter)) {
      counter++;
    }
  }
  return counter;
};

console.log(countVowels("Hello World"));




/* Write a function that takes an array of numbers and returns the sum of all the numbers in the array.
  Example:
  sumArray([1, 3, 4, 7, 9, 10]) == 34
  */

const sumArray = (arr) => {
  let sum = 0;
  for (let number of arr) {
    sum += number;
  }
  return sum;
};

console.log(sumArray([1, 3, 4, 7, 9, 10]));




/* Write a function that takes an array of numbers and returns the product of all the numbers in the array.
  Example:
  productArray([1, 3, 4, 7, 9, 10]) == 15120
  */

const productArray = (arr) => {
  let product = 1;
