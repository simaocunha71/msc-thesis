Here is the solution for the problem:

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

This function iterates over the list of operations and for each operation, it adds the value to the balance. If at any point the balance becomes negative, it returns `true`. If it iterates over the entire list without finding a negative balance, it returns `false`. The time complexity of this function is O(n), where n is the number of operations. The space complexity is O(1), as it only uses a constant amount of space to store the balance.