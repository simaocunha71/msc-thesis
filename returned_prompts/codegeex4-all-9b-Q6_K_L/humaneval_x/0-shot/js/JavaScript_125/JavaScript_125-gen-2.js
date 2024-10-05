```java
const splitWords = (txt) => {
  let t = txt.split(/\s/)
  if (t.length > 1) {
    return t
  }
  t = txt.split(/,/)
  if (t.length > 1) {
    return t
  }
  let p = 0
  for (let i = 0; i < txt.length; i++) {
    let c = txt[i].charCodeAt()
    if (c >= 97 && c <= 122 && c % 2 == 1) {
      p++
    }
  }
  return p
}
```
