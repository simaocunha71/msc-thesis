```java
const solve = (s) => {
  let letters = ''
  for (let i = 0; i < s.length; i++) {
    if (s[i] >= 'A' && s[i] <= 'Z' || s[i] >= 'a' && s[i] <= 'z') {
      letters += s[i]
    }
  }
  if (letters.length > 0) {
    let res = ''
    for (let i = 0; i < s.length; i++) {
      if (s[i] >= 'A' && s[i] <= 'Z' || s[i] >= 'a' && s[i] <= 'z') {
        res += letters[letters.length - 1]
        letters = letters.slice(0, letters.length - 1)
      } else {
        res += s[i]
      }
    }
    return res
  } else {
    let res = ''
    for (let i = s.length - 1; i >= 0; i--) {
      res += s[i]
    }
    return res
  }
}
```
