  // Ensure the values are in ascending order
  if (a > b) {
    [a, b] = [b, a];
  }

  // Initialize an array to store the even numbers
  let evenNumbers = [];

  // Loop from a to b
  for (let i = a; i <= b; i++) {
    // Check if the current number is even
    if (i % 2 === 0) {
      // If it is, add it to the array
      evenNumbers.push(i);
    }
  }

  // Return the array of even numbers
  return evenNumbers;
};

console.log(generateIntegers(2,8))
console.log(generateIntegers(8,2))
console.log(generateIntegers(10,14))

This function will work for any pair of positive integers. It starts from the smaller of the two numbers and goes up to the larger. For each number, it checks if it is even by seeing if the remainder of the number divided by 2 is 0 (which is the definition of an even number). If the number is even, it is added to an array that keeps track of all the even numbers. At the end, this array is returned.

*/

const generateIntegers = (a, b) => {
  if (a > b) {
    [a, b] = [b, a];
  }

  let evenNumbers = [];

  for (let i = a; i <= b; i++) {
    if (i % 2 === 0) {
      evenNumbers.push(i);
    }
  }

  return evenNumbers;
};

console.log(generateIntegers(2, 8)); // [2, 4, 6, 8]
console.log(generateIntegers(8, 2)); // [2, 4, 6, 8]
console.log(generateIntegers(10, 14)); // []

/*
  generateIntegers(2, 8) ➞ [2, 4, 6, 8]
  generateIntegers(8, 2) ➞