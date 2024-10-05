```java
const fruitDistribution = (s, n) => {
  let arr = s.split(' ')
  let apples = parseInt(arr[0])
  let oranges = parseInt(arr[4])
  return n - apples - oranges
}
```
