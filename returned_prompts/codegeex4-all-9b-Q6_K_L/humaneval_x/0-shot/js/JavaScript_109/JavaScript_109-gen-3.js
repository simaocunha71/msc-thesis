```java
const moveOneBall = (arr) => {
  if (arr.length == 0) { return true }
  var min = arr[0]
  var max = arr[0]
  var minIndex = 0
  var maxIndex = 0
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < min) {
      min = arr[i]
      minIndex = i
    }
    if (arr[i] > max) {
      max = arr[i]
      maxIndex = i
    }
  }
  if (maxIndex < minIndex) {
    return true
  } else {
    for (let i = 0; i < arr.length - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        return false
      }
    }
    return true
  }
}
```
