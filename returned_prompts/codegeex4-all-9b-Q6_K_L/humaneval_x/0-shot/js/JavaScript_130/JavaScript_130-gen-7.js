```java
const tri = (n) => {
  if (n == 0) return [0]
  if (n == 1) return [0, 1]
  if (n == 2) return [0, 1, 1]
  let a = 0, b = 1, c = 1, d = 0
  let ans = [0, 1, 1]
  for (let i = 3; i <= n; i++) {
    d = a + b + c
    ans.push(d)
    a = b
    b = c
    c = d
  }
  return ans
}
```
