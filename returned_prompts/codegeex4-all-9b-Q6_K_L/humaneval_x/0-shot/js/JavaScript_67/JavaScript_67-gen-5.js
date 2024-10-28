```java
const fruitDistribution = (s, n) => {
  var arr = s.split(/\s/)
  var apples = parseInt(arr[0])
  var oranges = parseInt(arr[4])
  return n - apples - oranges
}
```