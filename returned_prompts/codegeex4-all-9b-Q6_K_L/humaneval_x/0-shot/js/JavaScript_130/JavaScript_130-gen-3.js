```java
const tri = (n) => {
  if (n == 0) return [0]
  if (n == 1) return [0, 1]
  if (n == 2) return [0, 1, 1]
  let t = [0, 1, 1]
  for (let i = 3; i <= n; i++) {
    if (i % 2 == 0) t[i] = 1 + i / 2
    else t[i] = t[i - 1] + t[i - 2] + t[i - 3]
  }
  return t
}
```
