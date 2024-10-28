```java
const canArrange = (arr) => {
  let lo = 0
  let hi = arr.length - 1
  while (lo < hi) {
    if (arr[lo] > arr[hi]) return hi
    lo++
    if (lo === hi) return -1
    if (arr[lo] > arr[hi]) return hi
    hi--
  }
  return -1
}
```
