/*
  The idea is to calculate the sum of the first n numbers.
  Then we need to find the first number that is a multiple of 3.
  Once we have the first number, we need to find the second number that is also a multiple of 3.
  Once we have the first two numbers, we need to find the third number that is the sum of the first two numbers.
  Once we have all three numbers, we need to check if the sum of the three numbers is a multiple of 3.
  If it is, we increment the number of triples.
  If not, we move on to the next number.

  Time Complexity: O(n)
  Space Complexity: O(1)

  Example:
      Input: 5
      Output: 1
  */
  let sum = 0;
  let numberOfTriples = 0;
  let firstMultipleOfThree = 0;
  let secondMultipleOfThree = 0;
  let sumOfFirstTwoNumbers = 0;
  let isSumOfFirstTwoNumbersMultipleOfThree = false;

  // Calculate the sum of the first n numbers.
  for (let i = 1; i <= n; i++) {
    sum += i;
  }

  // Find the first number that is a multiple of 3.
  for (let i = 1; i <= n; i++) {
    if (sum % 3 === 0) {
      firstMultipleOfThree = sum;
      break;
    }
    sum--;
  }

  // Find the second number that is also a multiple of 3.
  for (let i = 1; i <= n; i++) {
    if (sum % 3 === 0) {
      secondMultipleOfThree = sum;
      break;
    }
    sum--;
  }

  // Find the third number that is the sum of the first two numbers.
  sumOfFirstTwoNumbers = firstMultipleOfThree + secondMultipleOfThree;
  isSumOfFirstTwoNumbersMultipleOfThree = sumOfFirstTwoNumbers % 3 === 0;

  // Check if the sum of the three numbers is a