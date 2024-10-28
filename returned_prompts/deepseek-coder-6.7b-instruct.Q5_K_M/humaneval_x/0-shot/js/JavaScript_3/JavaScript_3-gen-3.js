  let balance = 0;

  for (let i = 0; i < operations.length; i++) {
    balance += operations[i];
    if (balance < 0) return true;
  }

  return false;
}

console.log(belowZero([1, 2, 3])); // false
console.log(belowZero([1, 2, -4, 5])); // true
console.log(belowZero([100, -50, 25, -75])); // false
console.log(belowZero([100, -500, 25, -75])); // true
console.log(belowZero([])); // false

*/


// Solution:
function belowZero(operations) {
  let balance = 0;

  for (let i = 0; i < operations.length; i++) {
    balance += operations[i];
    if (balance < 0) return true;
  }

  return false;
}

console.log(belowZero([1, 2, 3])); // false
console.log(belowZero([1, 2, -4, 5])); // true
console.log(belowZero([100, -50, 25, -75])); // false
console.log(belowZero([100, -500, 25, -75])); // true
console.log(belowZero([])); // false



//  Note: The function belowZero(operations) iterates over the list of operations. For each operation, it adds the value of the operation to the current balance. If at any point the balance goes below zero, it immediately returns true. If the function finishes without finding a negative balance, it returns false.

// Time complexity: O(n) - n is the number of operations, as it needs to iterate over all the operations once.
// Space complexity: O(1) - the function uses a constant amount of additional space to store the balance and the current operation.


































