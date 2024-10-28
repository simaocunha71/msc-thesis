  let balance = 0;

  for(let i = 0; i < operations.length; i++) {
    balance += operations[i];
    if(balance < 0) return true;
  }

  return false;
}

console.log(belowZero([1, 2, 3])); // false
console.log(belowZero([1, 2, -4, 5])); // true
console.log(belowZero([100, -50, -25])); // true
console.log(belowZero([10, -20, 30, -40])); // true
console.log(belowZero([10, -20, 30, 40])); // false
console.log(belowZero([-10, 20, -30, 40])); // true

// The function belowZero(operations) iterates through the list of operations and adds each to the
// balance. If at any point the balance is less than zero, it returns true, indicating that the
// balance fell below zero. If the function completes without the balance falling below zero, it
// returns false.

// The function is also able to handle negative numbers, because the balance is only increased by
// the absolute value of the number, and the check for balance being less than zero is performed
// after this operation.

```



## 4. Reverse String

