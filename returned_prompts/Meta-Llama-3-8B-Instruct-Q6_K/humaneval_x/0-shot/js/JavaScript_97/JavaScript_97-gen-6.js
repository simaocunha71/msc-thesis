/*Your function should multiply the unit digits of the input numbers. 
The unit digit of a number is the last digit of the number.
For example, the unit digit of 148 is 8, the unit digit of 412 is 2, 
and the unit digit of 2020 is 0. 
In the given examples, the unit digits are 8 and 2, 9 and 8, 0 and 1, 4 and -5.

The function will multiply the unit digits of the input numbers and return the product.

Here is the complete function:
*/
const multiply = (a, b) => {
  // Extract the unit digits
  let unitA = Math.abs(a) % 10;
  let unitB = Math.abs(b) % 10;

  // Multiply the unit digits
  let product = unitA * unitB;

  // Return the product
  return product;
};

// Test the function
console.log(multiply(148, 412)); // Output: 16
console.log(multiply(19, 28)); // Output: 72
console.log(multiply(2020, 1851)); // Output: 0
console.log(multiply(14, -15)); // Output: 20
console.log(multiply(-19, -28)); // Output: 72

// Additional test cases
console.log(multiply(-148, 412)); // Output: 16
console.log(multiply(148, -412)); // Output: 16
console.log(multiply(-148, -412)); // Output: 16
console.log(multiply(-19, 28)); // Output: 72
console.log(multiply(19, -28)); // Output: 72
console.log(multiply(-19, -28)); // Output: 72
console.log(multiply(0, 0)); // Output: 0
console.log(multiply(0, 1)); // Output: 0
console.log(multiply(1, 0)); // Output: 0
console.log(multiply(1, 1)); // Output: 1
console.log(multiply(-1, 1)); // Output: 1
console.log(multiply(-1, -1)); // Output: 1
console.log(multiply(-1, 0)); // Output: 0
console.log(multiply(0, -1)); // Output: 0
console.log(multiply