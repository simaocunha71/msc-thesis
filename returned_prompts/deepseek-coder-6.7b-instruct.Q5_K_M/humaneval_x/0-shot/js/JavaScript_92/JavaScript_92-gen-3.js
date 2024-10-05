  return (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z)) && ((x === y + z) || (y === x + z) || (z === x + y));
}
console.log(anyInt(5, 2, 7)); // ➞ true
console.log(anyInt(3, 2, 2)); // ➞ false
console.log(anyInt(3, -2, 1)); // ➞ true
console.log(anyInt(3.6, -2.2, 2)); // ➞ false


// The function first checks if all inputs are integers, if not it returns false.
// Then, it checks if any of the numbers is equal to the sum of the other two. If so, it returns true.
// If not, it returns false.
// Number.isInteger() is a built-in function that checks if a number is an integer.
// The === operator checks for strict equality, meaning both value and type must match.
// The || operator is a logical OR operator, which returns true if either of the operands is true.
// In this case, it's used to check if any of the three numbers is equal to the sum of the other two.
// The parentheses are used to group the conditions, ensuring the correct order of operations.
// The function uses the short-circuit evaluation feature of the logical operators, so it doesn't evaluate the second operand if the first one is enough to determine the result.
// This makes the function more efficient and prevents potential errors.
// The function uses the ternary operator to simplify the code.
// The function uses the logical AND operator to ensure that all conditions must be true for the function to return true.
// If any of the conditions is not met, the function will return false.
// The function uses the built-in Number.isInteger() function to check if all numbers are integers.
// The function uses the === operator to check if the numbers are equal.
// The function uses the logical OR operator to check if any of the numbers is equal to the sum of the other two numbers.
// The function uses the parentheses to group the conditions and make the code more readable.
// The function uses the