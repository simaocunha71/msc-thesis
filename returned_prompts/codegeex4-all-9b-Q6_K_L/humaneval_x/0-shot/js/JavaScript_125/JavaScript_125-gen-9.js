```java
const splitWords = (txt) => {
  let t = txt.split(/\s/)
  if (t.length > 1) { return t }
  t = txt.split(/,/)
  if (t.length > 1) { return t }
  let c = 0
  for (let i = 0; i < txt.length; i++) {
    let v = txt[i].charCodeAt(0)
    if (v >= 97 && v <= 122 && v % 2 != 0) { c++ }
  }
  return c
}
```
