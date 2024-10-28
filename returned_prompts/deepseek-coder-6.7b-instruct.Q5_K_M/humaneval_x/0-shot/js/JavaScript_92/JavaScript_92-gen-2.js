  return (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z)) && ((x === y + z) || (y === x + z) || (z === x + y));
}

console.log(anyInt(5, 2, 7)) // ➞ true
console.log(anyInt(3, 2, 2)) // ➞ false
console.log(anyInt(3, -2, 1)) // ➞ true
console.log(anyInt(3.6, -2.2, 2)) // ➞ false

// Explanation:
// In the first example, 5 is equal to 2 + 7.
// In the second example, none of the numbers sum to the others, and all of them are integers.
// In the third example, -2 is equal to 1 - 4.
// In the fourth example, at least one of the numbers is not an integer.

*/

// Solution:
function anyInt(x, y, z) {
  return (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z)) && ((x === y + z) || (y === x + z) || (z === x + y));
}

console.log(anyInt(5, 2, 7)); // ➞ true
console.log(anyInt(3, 2, 2)); // ➞ false
console.log(anyInt(3, -2, 1)); // ➞ true
console.log(anyInt(3.6, -2.2, 2)); // ➞ false

// Explanation:
// In the first example, 5 is equal to 2 + 7.
// In the second example, none of the numbers sum to the others, and all of them are integers.
// In the third example, -2 is equal to 1 - 4.
// In the fourth example, at least one of the numbers is not an integer.

module.exports = anyInt;
