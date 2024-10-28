```java
const validDate = (date) => {
  if (date == '') return false;
  let [m,d,y] = date.split('-');
  if (m < 1 || m > 12) return false;
  if (d < 1 || d > 31) return false;
  if ((m == 4 || m == 6 || m == 9 || m == 11) && d > 30) return false;
  if (m == 2) {
    if (y % 4 == 0) {
      if (d > 29) return false;
    }
    else if (d > 28) return false;
  }
  return true;
}
```
