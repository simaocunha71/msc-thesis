```java
const solve = (N) => {
  const digits = N.toString(2).split('');
  return digits.reduce((a, b) => a + parseInt(b), 0).toString(2);
}
```
