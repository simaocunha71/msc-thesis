```java
const solve = (s) => {
  let ar = []
  let isLetter = false
  for (let i = 0; i < s.length; i++) {
    if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z')) {
      isLetter = true
      ar.push(s[i])
    } else {
      ar.push(s[i])
    }
  }
  if (isLetter) {
    for (let i = 0; i < ar.length; i++) {
      if ((ar[i] >= 'a' && ar[i] <= 'z')) {
        ar[i] = ar[i].toUpperCase()
      } else if ((ar[i] >= 'A' && ar[i] <= 'Z')) {
        ar[i] = ar[i].toLowerCase()
      }
    }
    return ar.join('')
  } else {
    return ar.reverse().join('')
  }
}
```