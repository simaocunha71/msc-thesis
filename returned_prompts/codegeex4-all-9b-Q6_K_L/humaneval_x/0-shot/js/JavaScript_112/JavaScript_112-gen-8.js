```java
const reverseDelete = (s, c) => {
  let p = ''
  for (let i = 0; i < s.length; i++) {
    if (!c.includes(s[i])) {
      p += s[i]
    }
  }
  let q = p.split('').reverse().join('')
  return [p, p == q]
}
```
