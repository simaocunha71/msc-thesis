```java
const fruitDistribution = (s, n) => {
  let splitted = s.split(' ')
  let apples = parseInt(splitted[0])
  let oranges = parseInt(splitted[4])
  return n - apples - oranges
}
```