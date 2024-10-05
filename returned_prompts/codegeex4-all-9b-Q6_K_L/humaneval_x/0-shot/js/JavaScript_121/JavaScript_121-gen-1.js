```java
const solution = (lst) => {
  var sum = 0;
  for (let i = 0; i < lst.length; i += 2) {
    if (lst[i] % 2 !== 0) {
      sum += lst[i];
    }
  }
  return sum;
}
```
The solution iterates over the list in steps of two (i.e., only even indices), and checks if the value at that index is odd. If it is, it adds it to the sum. Finally, it returns the sum.