```java
const solve = (s) => {
  let r = ''
  let c = false
  for (let i = 0; i < s.length; i++) {
    if (s[i].match(/[a-z]/i)) {
      c = !c
      r += c ? s[i].toUpperCase() : s[i].toLowerCase()
    } else {
      r += s[i]
    }
  }
  return c ? r.split('').reverse().join('') : r
}
```
