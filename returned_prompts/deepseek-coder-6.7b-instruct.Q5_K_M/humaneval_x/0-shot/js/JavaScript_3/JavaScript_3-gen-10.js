  let balance = 0;
  for (let operation of operations) {
    balance += operation;
    if (balance < 0) {
      return true;
    }
  }
  return false;
};

console.log(belowZero([1, 2, 3])); // false
console.log(belowZero([1, 2, -4, 5])); // true
console.log(belowZero([100, -50, -75])); // true
console.log(belowZero([100, -50, 25])); // false

// Explanation:
// For the first case, balance is [1, 3, 6] and never falls below zero.
// For the second case, balance is [1, 3, -1, 4] and falls below zero at the third operation.
// For the third case, balance is [100, 50, -25] and falls below zero at the second operation.
// For the fourth case, balance is [100, 50, 75] and never falls below zero.

// This solution runs in O(n) time complexity where n is the number of operations.

// I hope this helps you to understand the problem. If you have any more questions, feel free to ask.

module.exports = belowZero;

// This function takes an array of integers representing operations on a bank account.
// It starts with a balance of 0 and iterates through the array, adding the value of each operation to the balance.
// If at any point the balance is less than 0, the function immediately returns true.
// If the function completes the iteration without the balance ever being less than 0, it returns false.
// This demonstrates a simple way to detect if a bank account balance ever falls below zero.
```

## 5. 클래스와 객체

```javascript
// 