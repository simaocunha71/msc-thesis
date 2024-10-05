```java
const moveOneBall = (arr) => {
  if (arr.length == 0) { return true }
  let arr1 = arr.slice()
  let arr2 = arr.slice()
  arr1.push(...arr1)
  arr2.push(...arr2)
  arr1 = arr1.slice(0, arr2.length)
  for (let i = 0; i < arr1.length; i++) {
    if (JSON.stringify(arr1) === JSON.stringify(arr2.sort((a, b) => a - b).slice(i))) {
      return true
    }
  }
  return false
}
```
