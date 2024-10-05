```java
const reverseDelete = (s, c) => {
  let t = ''
  for (let i = 0; i < s.length; i++) {
    if (!c.includes(s[i])) {
      t += s[i]
    }
  }
  let rev = ''
  for (let i = t.length - 1; i >= 0; i--) {
    rev += t[i]
  }
  return [t, rev == t]
}
```
