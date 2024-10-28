```java
const derivative = (xs) => {
  const result = [];
  for (let i = 1; i < xs.length; i++) {
    result.push(xs[i] * i);
  }
  return result;
}
```