Here is a possible solution in JavaScript:
```
const belowZero = (operations) => {
  let balance = 0;
  for (const operation of operations) {
    balance += operation;
    if (balance < 0) {
      return true;
    }
  }
  return false;
};
```
Explanation:

* We initialize the `balance` variable to 0, which represents the initial balance of the account.
* We iterate over the `operations` array using a `for...of` loop.
* For each operation, we add it to the `balance` variable.
* We check if the `balance` falls below 0. If it does, we immediately return `true`, indicating that the balance went below zero at some point.
* If we reach the end of the loop without finding a negative balance, we return `false`, indicating that the balance never fell below zero.

You can test this function with the examples you provided:
```
console.log(belowZero([1, 2, 3])); // false
console.log(belowZero([1, 2, -4, 5])); // true
``` A more functional way to solve this problem is to use the `reduce` method:
```
const belowZero = (operations) => operations.reduce((balance, operation) => balance + operation, 0) < 0;
```
This solution is more concise and uses the `reduce` method to accumulate the operations and check if the balance falls below 0.