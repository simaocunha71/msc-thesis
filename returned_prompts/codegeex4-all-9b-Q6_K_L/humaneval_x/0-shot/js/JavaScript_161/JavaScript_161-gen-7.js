```java
const solve = (s) => {
  let r = ''
  let isLetter = false
  for (let i = 0; i < s.length; i++) {
    if (/[a-zA-Z]/.test(s[i])) {
      isLetter = true
      if (/[a-z]/.test(s[i])) {
        r += s[i].toUpperCase()
      } else {
        r += s[i].toLowerCase()
      }
    } else {
      r += s[i]
    }
  }
  if (!isLetter) {
    r = r.split('').reverse().join('')
  }
  return r
}
```