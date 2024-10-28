```java
const wordsString = (s) => {
  let t = ""
  let p = []
  for (let i = 0; i < s.length; i++) {
    if (s[i] == ',') {
      p.push(t)
      t = ""
    } else if (s[i] == ' ') {
      continue
    } else {
      t += s[i]
    }
  }
  p.push(t)
  return p
}
```
