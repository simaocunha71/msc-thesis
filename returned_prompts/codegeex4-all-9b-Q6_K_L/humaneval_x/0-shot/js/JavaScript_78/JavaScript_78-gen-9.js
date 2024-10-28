```java
const hexKey = (num) => {
  let t = 0
  let hex = '2357BDF'
  for (let i = 0; i < num.length; i++) {
    if (hex.includes(num[i])) { t++ }
  }
  return t
}
```
