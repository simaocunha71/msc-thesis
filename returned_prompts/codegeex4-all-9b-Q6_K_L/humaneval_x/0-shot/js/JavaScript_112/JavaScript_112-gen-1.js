```java
const reverseDelete = (s, c) => {
  let t = ''
  for (let i = 0; i < s.length; i++) {
    if (!c.includes(s[i])) t += s[i]
  }
  for (let i = 0; i < t.length / 2; i++) {
    if (t[i] != t[t.length - 1 - i]) return [t, false]
  }
  return [t, true]
}
```
