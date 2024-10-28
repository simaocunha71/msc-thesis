```java
const reverseDelete = (s, c) => {
  let t = ''
  for (let i = 0; i < s.length; i++) {
    if (c.indexOf(s[i]) === -1) {
      t += s[i]
    }
  }
  let rev = ''
  for (let i = t.length - 1; i >= 0; i--) {
    rev += t[i]
  }
  return [t, t === rev]
}
```
