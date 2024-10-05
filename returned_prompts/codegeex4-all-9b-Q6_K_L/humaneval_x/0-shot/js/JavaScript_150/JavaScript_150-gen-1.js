```java
const xOrY = (n, x, y) => {
  for (let i = 2; i < n; i++)
    if (n % i === 0) return y;
  return x;
}
```