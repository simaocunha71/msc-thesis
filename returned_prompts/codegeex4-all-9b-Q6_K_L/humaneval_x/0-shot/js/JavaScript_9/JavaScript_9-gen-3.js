```js
const rollingMax = (numbers) => {
  let max = numbers[0]
  return numbers.map(n => {
    if (n > max) max = n
    return max
  })
}
```
