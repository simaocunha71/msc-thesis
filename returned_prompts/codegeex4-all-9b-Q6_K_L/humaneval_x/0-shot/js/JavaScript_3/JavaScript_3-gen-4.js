```java
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
