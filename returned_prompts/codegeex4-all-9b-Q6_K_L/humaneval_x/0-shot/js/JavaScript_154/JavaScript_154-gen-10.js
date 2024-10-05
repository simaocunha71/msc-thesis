```java
const cycpatternCheck = (a, b) => {
  var c = b + b
  for (let i = 0; i < a.length; i++) {
    if (a.slice(i, i + b.length) == b || a.slice(i, i + b.length) == c.slice(0, b.length)) return true
  }
  return false
}
```
