  const getUnitDigit = number => Math.abs(number % 10);
  return getUnitDigit(a) * getUnitDigit(b);
}

console.log(multiply(148, 412)); // should return 16
console.log(multiply(19, 28)); // should return 72
console.log(multiply(2020, 1851)); // should return 0
console.log(multiply(14,-15)); // should return 20

// 1. Create a function named "getUnitDigit" that takes a number as an argument and returns its unit digit by taking the absolute value of the remainder when the number is divided by 10.

// 2. Return the product of the unit digits of a and b by calling the "getUnitDigit" function on them.

// 3. Call the "multiply" function with the required arguments and log the results to the console.
  


// Function to get the unit digit of a number
const getUnitDigit = number => Math.abs(number % 10);

// Function to multiply two numbers' unit digits
const multiply = (a, b) => {
  return getUnitDigit(a) * getUnitDigit(b);
}

// Test the function
console.log(multiply(148, 412)); // should return 16
console.log(multiply(19, 28)); // should return 72
console.log(multiply(2020, 1851)); // should return 0
console.log(multiply(14,-15)); // should return 20



































































































