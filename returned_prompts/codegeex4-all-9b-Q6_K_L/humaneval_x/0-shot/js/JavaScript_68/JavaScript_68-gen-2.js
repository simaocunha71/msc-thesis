```java
const pluck = (arr) => {
  let min = Infinity
  let index = -1
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0) {
      if (arr[i] < min) {
        min = arr[i]
        index = i
      }
    }
  }
  if (index === -1) return []
  return [min, index]
}
```
