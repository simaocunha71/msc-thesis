```java
const moveOneBall = (arr) => {
  let t = arr.length
  let k = 0
  for (let i = 0; i < t; i++) {
    if (arr[i] < arr[i + 1]) {
      k++
    }
  }
  if (k === t - 1) return true
  return false
}
```
