```java
const validDate = (date) => {
  var arr = date.split(/-/)
  if (arr.length != 3) return false
  if (arr[0] < 1 || arr[0] > 12) return false
  if (arr[2] < 1 || arr[2] > 29) return false
  if (arr[0] == 2) {
    if (arr[2] > 29) return false
    if (arr[2] == 29) {
      if (arr[0] != 2 || arr[2] != 29 || arr[1] > 2 || arr[1] < 1) return false
    }
  }
  if (arr[0] == 4 || arr[0] == 6 || arr[0] == 9 || arr[0] == 11) {
    if (arr[2] > 30) return false
  }
  if (arr[2] > 31) return false
  if (arr[2] == 31) {
    if (arr[0] != 1 || arr[0] != 3 || arr[0] != 5 || arr[0] != 7 || arr[0] != 8 || arr[0] != 10 || arr[0] != 12) return false
  }
  return true
}
```
