```java
const selectWords = (s, n) => {
  let t = s.split(/\s/)
  let p = []
  for (let j = 0; j < t.length; j++) {
    let k = 0
    for (let i = 0; i < t[j].length; i++) {
      if (t[j][i] !== 'a' && t[j][i] !== 'e' && t[j][i] !== 'i' && t[j][i] !== 'o' && t[j][i] !== 'u' && t[j][i] !== 'A' && t[j][i] !== 'E' && t[j][i] !== 'I' && t[j][i] !== 'O' && t[j][i] !== 'U') {
        k++
      }
    }
    if (k === n) {
      p.push(t[j])
    }
  }
  return p
}
```
