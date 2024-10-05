```java
const pluck = (arr) => {
  if (arr.length == 0) return []
  var min = Number.MAX_SAFE_INTEGER
  var minIndex = -1
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0 && arr[i] <= min) {
      min = arr[i]
      minIndex = i
    }
  }
  if (min == Number.MAX_SAFE_INTEGER) return []
  return [min, minIndex]
}
```
