```java
const digitSum = (s) => {
  let total = 0
  for (let i = 0; i < s.length; i++) {
    let c = s[i]
    if (c === c.toUpperCase()) {
      total += c.charCodeAt(0)
    }
  }
  return total
}
```
