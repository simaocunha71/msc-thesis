```js
const generateIntegers = (a, b) => {
  if (a > b) [a, b] = [b, a]
  let res = []
  for (let i = a; i <= b; i++) {
    if (i % 2 === 0) res.push(i)
  }
  return res
}
```