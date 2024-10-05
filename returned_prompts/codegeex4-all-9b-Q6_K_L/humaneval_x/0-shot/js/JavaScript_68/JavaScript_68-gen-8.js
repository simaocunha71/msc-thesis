```js
const pluck = (arr) => {
  if (arr.length === 0) return []
  let smallest = Infinity
  let index = -1
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < smallest) {
      smallest = arr[i]
      index = i
    }
  }
  if (index === -1) return []
  return [smallest, index]
}
```
