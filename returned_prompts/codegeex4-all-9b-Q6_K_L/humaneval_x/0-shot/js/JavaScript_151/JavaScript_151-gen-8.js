```java
const doubleTheDifference = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    let num = lst[i];
    if (num % 2 !== 0 && num >= 0 && Number.isInteger(num)) {
      sum += num * num;
    }
  }
  return sum;
}
```
