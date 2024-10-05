The problem can be solved by maintaining a running balance and checking if it falls below zero at any point in the operations list. Here is the solution in JavaScript:

```javascript
const belowZero = (operations) => {
  let balance = 0;
  for (let i = 0; i < operations.length; i++) {
    balance += operations[i];
    if (balance < 0) {
      return true;
    }
  }
  return false;
};
```

This solution iterates over the operations list and updates the balance by adding each operation to it. If at any point the balance becomes negative, it returns true. If the loop completes without the balance falling below zero, it returns false.