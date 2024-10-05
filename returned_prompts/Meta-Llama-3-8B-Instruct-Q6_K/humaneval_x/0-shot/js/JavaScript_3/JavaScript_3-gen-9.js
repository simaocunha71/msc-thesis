Here is the solution in JavaScript:

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

Explanation:
The function `belowZero` takes a list of operations as input. It initializes the balance to 0. Then it iterates over the operations. For each operation, it adds the operation to the balance. If at any point the balance falls below 0, it returns `true`. If it finishes iterating over all operations without the balance falling below 0, it returns `false`. The `for` loop iterates over the operations, and the `if` statement checks if the balance is less than 0. If it is, the function returns `true`. If the loop finishes without the balance falling below 0, the function returns `false`. This function simulates a bank account and checks if the account balance ever falls below 0. If it does, the function returns `true`; otherwise, it returns `false`. The function can be called with a list of operations, such as `belowZero([1, 2, 3])` or `belowZero([1, 2, -4, 5])`. The function will return `false` for the first example and `true` for the second example.