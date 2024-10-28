```java
const validDate = (date) => {
  if (date.length == 0) return false
  var [m, d, y] = date.split('-')
  m = Number(m)
  d = Number(d)
  y = Number(y)
  if (m < 1 || m > 12) return false
  if ((m == 4 || m == 6 || m == 9 || m == 11) && (d < 1 || d > 30)) return false
  if ((m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12) && (d < 1 || d > 31)) return false
  if (m == 2) {
    if (d < 1 || d > 29) return false
    if (d == 29 && !((y % 4 == 0 && y % 100 != 0) || y % 400 == 0)) return false
  }
  return true
}
```
