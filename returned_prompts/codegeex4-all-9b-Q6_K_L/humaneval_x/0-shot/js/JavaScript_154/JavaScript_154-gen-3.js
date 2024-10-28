```java
const cycpatternCheck = (a, b) => {
  let n = b.length
  for (let i = 0; i < n; i++) {
    let s = b.slice(i) + b.slice(0, i)
    if (a.includes(s)) return true
  }
  return false
}
```
