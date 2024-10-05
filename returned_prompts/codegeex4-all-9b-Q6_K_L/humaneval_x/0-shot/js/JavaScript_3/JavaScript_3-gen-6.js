Here's the solution:
```
const belowZero = (operations) => {
  let balance = 0;
  for (let i = 0; i < operations.length; i++) {
    balance += operations[i];
    if (balance < 0) {
      return true;
    }
  }
  return false;
}
```
Explanation:
- We initialize a variable `balance` to 0, which represents the current balance of the bank account.
- We then iterate through the `operations` array using a `for` loop.
- In each iteration, we add the current operation to the `balance`.
- If at any point the `balance` falls below zero, we return `true`.
- If the `balance` never falls below zero throughout the iteration, we return `false` after the loop finishes.