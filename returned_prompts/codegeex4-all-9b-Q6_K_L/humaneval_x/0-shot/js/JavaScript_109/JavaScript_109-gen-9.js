```java
const moveOneBall = (arr) => {
  if (arr.length == 0) { return true }
  let min = arr[0]
  let minIndex = 0
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < min) {
      min = arr[i]
      minIndex = i
    }
  }
  for (let i = minIndex; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) { return false }
  }
  for (let i = 0; i < minIndex - 1; i++) {
    if (arr[i] > arr[i + 1]) { return false }
  }
  return true
}
```
