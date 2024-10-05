  return (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z)) && (x === y + z || y === x + z || z === x + y);
}

console.log(anyInt(5, 2, 7)); // true
console.log(anyInt(3, 2, 2)); // false
console.log(anyInt(3, -2, 1)); // true
console.log(anyInt(3.6, -2.2, 2)); // false
console.log(anyInt(3, 2.5, 4)); // false

// ➞ true because 3 is equal to 2 + 1
// ➞ false because one of the numbers is a non-integer (3.6)
// ➞ false because 2.5 is not an integer

Explanation: 
This program checks if all the inputs are integers and if one of the inputs is equal to the sum of the other two. It uses the Number.isInteger() function to check if a number is an integer, and the === operator to check if two values are equal.
The function returns true if both conditions are met, and false otherwise.
*/

/*
