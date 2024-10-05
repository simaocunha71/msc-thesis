```js
const doubleTheDifference = (lst) => {
  let sum = 0
  for (let i = 0; i < lst.length; i++) {
    const num = lst[i]
    if (num > 0 && Number.isInteger(num) && num % 2 !== 0) {
      sum += num * num
    }
  }
  return sum
}
```
