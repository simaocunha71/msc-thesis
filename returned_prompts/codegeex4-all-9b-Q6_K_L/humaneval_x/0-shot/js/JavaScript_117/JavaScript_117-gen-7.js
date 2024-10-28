```java
const selectWords = (s, n) => {
  var t = s.split(/\s/)
  var p = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
  var r = []
  for (let i = 0; i < t.length; i++) {
    var q = 0
    for (let j = 0; j < t[i].length; j++) {
      if (p.indexOf(t[i][j]) > -1) q++
    }
    if (q == n) r.push(t[i])
  }
  return r
}
```
