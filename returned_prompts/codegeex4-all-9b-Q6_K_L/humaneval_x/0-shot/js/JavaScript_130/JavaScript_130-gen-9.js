```java
const tri = (n) => {
  if (n == 0) {
    return [1];
  }
  if (n == 1) {
    return [1, 3];
  }
  if (n == 2) {
    return [1, 3, 2];
  }
  if (n == 3) {
    return [1, 3, 2, 8];
  }
  let result = [1, 3, 2, 8];
  for (let i = 4; i <= n; i++) {
    if (i % 2 == 0) {
      result.push(1 + i / 2);
    } else {
      result.push(result[i - 1] + result[i - 2] + result[i - 3]);
    }
  }
  return result;
}
```
