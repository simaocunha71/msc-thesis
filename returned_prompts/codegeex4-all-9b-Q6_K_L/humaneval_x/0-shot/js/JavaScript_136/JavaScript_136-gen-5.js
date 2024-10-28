```js
const largestSmallestIntegers = (lst) => {
  let positives = lst.filter(x => x > 0).sort((a, b) => a - b);
  let negatives = lst.filter(x => x < 0).sort((a, b) => b - a);
  let res = [null, null];
  if (positives.length > 0) res[1] = positives[0];
  if (negatives.length > 0) res[0] = negatives[0];
  return res;
}
```