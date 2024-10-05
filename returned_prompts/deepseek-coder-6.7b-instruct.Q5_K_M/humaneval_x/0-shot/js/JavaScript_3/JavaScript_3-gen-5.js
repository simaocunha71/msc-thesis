  let balance = 0;
  for (let operation of operations) {
    balance += operation;
    if (balance < 0) {
      return true;
    }
  }
  return false;
}

console.log(belowZero([1, 2, 3])); // false
console.log(belowZero([1, 2, -4, 5])); // true

This function works by iterating over the operations list and adding each one to the current balance. If at any point the balance is less than zero, the function immediately returns true. If it finishes the loop without ever finding a negative balance, it returns false.

*/

/*
  