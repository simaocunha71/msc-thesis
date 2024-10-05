```js
const prodSigns = (arr) => {
  if (!arr.length) return null
  const prod = arr.reduce((acc, val) => acc * val, 1)
  const signs = arr.map(val => Math.sign(val))
  const signProduct = signs.reduce((acc, val) => acc * val, 1)
  return Math.abs(prod) * signProduct
}
```
