```java
const fruitDistribution = (s, n) => {
  const arr = s.split(" ");
  let apples = 0, oranges = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "apples") apples = Number(arr[i - 1]);
    if (arr[i] === "oranges") oranges = Number(arr[i - 1]);
  }
  return n - apples - oranges;
}
```
