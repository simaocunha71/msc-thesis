```js
const fruitDistribution = (s, n) => {
  let [a, b] = s.split("apples and");
  let apples = parseInt(a);
  let oranges = parseInt(b);
  return n - apples - oranges;
}
```
