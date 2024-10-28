```java
const fruitDistribution = (s, n) => {
  let arr = s.split(' ');
  let apples = Number(arr[0]);
  let oranges = Number(arr[4]);
  return n - apples - oranges;
}
```
