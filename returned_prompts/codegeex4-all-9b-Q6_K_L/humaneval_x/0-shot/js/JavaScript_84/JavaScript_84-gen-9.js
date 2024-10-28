```java
const solve = (N) => {
  let bin = N.toString(2);
  let sum = 0;
  for (let i = 0; i < bin.length; i++) {
    sum += parseInt(bin[i]);
  }
  return sum.toString(2);
}
```
