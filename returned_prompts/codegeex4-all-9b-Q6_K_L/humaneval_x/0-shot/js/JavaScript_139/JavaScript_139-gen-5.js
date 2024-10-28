```java
const specialFactorial = (n) => {
  if (n < 1) return 1;
  let result = 1;
  for (let i = n; i > 0; i--) {
    result *= factorial(i);
  }
  return result;
}

const factorial = (n) => {
  if (n < 1) return 1;
  return n * factorial(n - 1);
}
```
