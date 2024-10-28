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
The `belowZero` function takes a list of operations as input and returns a boolean value indicating whether the balance of the account falls below zero at any point. The function initializes the balance to zero and then iterates over the operations. For each operation, it adds the operation to the balance. If the balance becomes negative, it returns `true` immediately. If the function iterates over all operations without finding a negative balance, it returns `false`. The time complexity of this function is O(n), where n is the number of operations, as it needs to iterate over all operations. The space complexity is O(1), as it only uses a constant amount of space to store the balance. This function passes the given test cases.