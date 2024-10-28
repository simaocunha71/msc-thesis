```java
const reverseDelete = (s, c) => {
  var t = s.split('')
  for (var i = 0; i < c.length; i++) {
    t = t.filter(x => x != c[i])
  }
  var u = t.join('')
  var v = u.split('').reverse().join('')
  if (u == v) {
    return [u, true]
  } else {
    return [u, false]
  }
}
```
