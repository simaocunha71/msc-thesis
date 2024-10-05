```java
const solve = (s) => {
  let t = ''
  let f = 0
  for (let i = 0; i < s.length; i++) {
    if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z')) {
      f = 1
      if (s[i] === s[i].toLowerCase()) { t += s[i].toUpperCase() }
      else { t += s[i].toLowerCase() }
    }
    else {
      t += s[i]
    }
  }
  if (f === 0) { t = s.split('').reverse().join('') }
  return t
}
```