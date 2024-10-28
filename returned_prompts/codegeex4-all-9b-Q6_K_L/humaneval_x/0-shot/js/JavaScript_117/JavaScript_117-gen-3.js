```java
const selectWords = (s, n) => {
  var t = s.split(/\s/)
  var y = []
  for (var i = 0; i < t.length; i++) {
    var u = t[i].replace(/[^bcdfghjklmnpqrstvwxyz]/gi, '')
    if (u.length == n) {
      y.push(t[i])
    }
  }
  return y
}
```
