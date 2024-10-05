```java
const validDate = (date) => {
  let split = date.split('-')
  if (split.length != 3) { return false }
  let m = parseInt(split[0])
  let d = parseInt(split[1])
  let y = parseInt(split[2])
  if (m < 1 || m > 12) { return false }
  if (d < 1 || d > 31) { return false }
  if ((m == 4 || m == 6 || m == 9 || m == 11) && d > 30) { return false }
  if ((m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12) && d > 31) { return false }
  if (m == 2) {
    if (d > 29) { return false }
    if (y % 4 == 0 && (y % 100 != 0 || y % 400 == 0) && d > 28) { return false }
  }
  return true
}
```
