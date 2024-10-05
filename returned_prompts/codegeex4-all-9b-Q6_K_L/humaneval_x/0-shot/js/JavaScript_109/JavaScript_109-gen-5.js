```java
const moveOneBall = (arr) => {
  if (arr.length === 0) { return true }
  let min = Math.min(...arr)
  let minIdx = arr.indexOf(min)
  let sortedArr = arr.slice(minIdx).concat(arr.slice(0, minIdx))
  for (let i = 0; i < arr.length - 1; i++) {
    if (sortedArr[i] > sortedArr[i + 1]) { return false }
  }
  return true
}
```
