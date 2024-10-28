```java
const solve = (s) => {
  let s2 = ''
  let l = 0
  let r = s.length - 1
  for (let i = 0; i < s.length; i++) {
    if (s[i] >= 'a' && s[i] <= 'z' || s[i] >= 'A' && s[i] <= 'Z') {
      s2 += s[i] == s[i].toLowerCase() ? s[i].toUpperCase() : s[i].toLowerCase()
    } else {
      s2 += s[i]
    }
    if (i != r) {
      if (s[i] >= 'a' && s[i] <= 'z' || s[i] >= 'A' && s[i] <= 'Z') {
        s2 += s[r] == s[r].toLowerCase() ? s[r].toUpperCase() : s[r].toLowerCase()
      } else {
        s2 += s[r]
      }
      r--
    }
  }
  return s2
}
```