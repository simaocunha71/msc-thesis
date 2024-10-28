```java
const validDate = (date) => {
  var parts = date.split('-');
  if (parts.length != 3) { return false; }
  var m = parseInt(parts[0]);
  var d = parseInt(parts[1]);
  var y = parseInt(parts[2]);
  if (isNaN(m) || isNaN(d) || isNaN(y)) { return false; }
  if (m < 1 || m > 12) { return false; }
  if (d < 1) { return false; }
  if (m == 2) {
    if (d > 29) { return false; }
    if (d == 29) {
      if (y % 4 != 0) { return false; }
      if (y % 100 == 0 && y % 400 != 0) { return false; }
    }
  } else if ([4,6,9,11].includes(m)) {
    if (d > 30) { return false; }
  } else {
    if (d > 31) { return false; }
  }
  return true;
}
```
