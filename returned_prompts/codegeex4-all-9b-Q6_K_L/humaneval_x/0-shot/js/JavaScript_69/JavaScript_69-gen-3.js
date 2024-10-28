```js
const search = (lst) => {
  let max = -1
  let counts = lst.reduce((acc, num) => {
    acc[num] = (acc[num] || 0) + 1
    return acc
  }, {})
  for (let num in counts) {
    if (counts[num] >= num && num > max) {
      max = num
    }
  }
  return max
}
```
