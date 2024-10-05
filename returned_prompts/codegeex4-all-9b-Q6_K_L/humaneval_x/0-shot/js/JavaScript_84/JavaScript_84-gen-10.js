```java
const solve = (N) => {
  var binary = N.toString(2);
  var sum = 0;
  for (let i = 0; i < binary.length; i++) {
    sum += parseInt(binary[i]);
  }
  return sum.toString(2);
}
```
