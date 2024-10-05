```java
const splitWords = (txt) => {
  let arr = txt.split(/\s/)
  if (arr.length > 1) {
    return arr
  } else {
    arr = txt.split(/,/)
    if (arr.length > 1) {
      return arr
    } else {
      let n = 0
      for (let i = 0; i < txt.length; i++) {
        let c = txt[i]
        if (c >= 'a' && c <= 'z') {
          if (c.charCodeAt() % 2 == 1) {
            n += 1
          }
        }
      }
      return n
    }
  }
}
```
