```java
const tri = (n) => {
  if (n == 0)
    return [0]
  if (n == 1)
    return [0, 1]
  if (n == 2)
    return [0, 1, 1]
  var out = [0, 1, 1]
  for (let i = 3; i <= n; i++) {
    if (i % 2 == 0)
      out.push(1 + i / 2)
    else
      out.push(out[i - 1] + out[i - 2] + out[i - 3])
  }
  return out
}
```
