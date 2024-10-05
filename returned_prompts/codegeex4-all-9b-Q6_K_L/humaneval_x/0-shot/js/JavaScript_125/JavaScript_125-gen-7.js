```java
const splitWords = (txt) => {
  if (txt.indexOf(' ') !== -1) { return txt.split(' ') }
  if (txt.indexOf(',') !== -1) { return txt.split(',') }
  let count = 0
  for (let i = 0; i < txt.length; i++) {
    let ord = txt.charCodeAt(i)
    if (ord >= 97 && ord <= 122 && (ord % 2) !== 0) {
      count++
    }
  }
  return count
}
```
