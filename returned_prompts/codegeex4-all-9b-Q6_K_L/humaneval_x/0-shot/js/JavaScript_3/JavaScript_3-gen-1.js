Here is the solution:

```javascript
const belowZero = (operations) => {
  let balance = 0;
  for (let operation of operations) {
    balance += operation;
    if (balance < 0) {
      return true;
    }
  }
  return false;
}
```

This function works by iterating over each operation in the `operations` array. It adds each operation to the `balance` variable. If at any point the `balance` falls below zero, the function returns `true`. If the function finishes iterating over all operations without the `balance` falling below zero, it returns `false`.