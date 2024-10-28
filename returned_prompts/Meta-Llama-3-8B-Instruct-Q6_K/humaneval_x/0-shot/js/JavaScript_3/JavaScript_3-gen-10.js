Here is the solution to the problem:
```
const belowZero = (operations) => {
  let balance = 0;
  for (let operation of operations) {
    balance += operation;
    if (balance < 0) {
      return true;
    }
  }
  return false;
};
```
Explanation:

* We initialize the `balance` variable to 0, which represents the initial balance of the bank account.
* We iterate through the `operations` array, adding each operation to the `balance`.
* If the `balance` falls below 0 at any point, we immediately return `true`.
* If we finish iterating through the array without the balance falling below 0, we return `false`.

Testing:

```
console.log(belowZero([1, 2, 3])); // false
console.log(belowZero([1, 2, -4, 5])); // true
```
Output:
```
false
true
```


The code will return `true` if the balance falls below 0 at any point and `false` otherwise.