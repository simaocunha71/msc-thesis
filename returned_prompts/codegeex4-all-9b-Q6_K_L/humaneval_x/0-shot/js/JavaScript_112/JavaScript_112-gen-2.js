```java
const reverseDelete = (s, c) => {
  let t = ''
  for (let i = 0; i < s.length; i++) {
    if (!c.includes(s[i])) {
      t += s[i]
    }
  }
  return [t, t === t.split('').reverse().join('')]
}
```
