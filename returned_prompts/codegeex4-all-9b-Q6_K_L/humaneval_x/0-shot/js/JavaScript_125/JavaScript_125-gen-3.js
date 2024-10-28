```java
const splitWords = (txt) => {
  let t = txt.split(/\s/)
  if (t.length > 1) { return t }
  t = txt.split(',')
  if (t.length > 1) { return t }
  let c = 0
  for (let i = 0; i < txt.length; i++) {
    let o = txt[i].charCodeAt()
    if (o >= 97 && o <= 122 && o % 2 == 1) { c++ }
  }
  return c
}
```
