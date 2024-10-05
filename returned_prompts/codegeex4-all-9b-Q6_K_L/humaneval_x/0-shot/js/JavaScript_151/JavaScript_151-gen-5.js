```javascript
const doubleTheDifference = (lst) => {
  let result = 0
  for (let i = 0; i < lst.length; i++) {
    let num = lst[i]
    if (num < 0 || !Number.isInteger(num) || num % 2 === 0) {
      continue
    }
    result += num * num
  }
  return result * 2
}
```