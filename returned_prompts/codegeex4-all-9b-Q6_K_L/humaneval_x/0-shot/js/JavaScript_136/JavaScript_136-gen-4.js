```js
const largestSmallestIntegers = (lst) => {
  const negatives = lst.filter(n => n < 0).sort((a, b) => b - a)
  const positives = lst.filter(n => n > 0).sort((a, b) => a - b)
  return [negatives[0] || null, positives[0] || null]
}
```
