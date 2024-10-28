```java
const digitSum = (s) => {
  let sum = 0
  for (let i = 0; i < s.length; i++) {
    let char = s[i]
    if (char >= 'A' && char <= 'Z') {
      sum += char.charCodeAt(0)
    }
  }
  return sum
}
```
