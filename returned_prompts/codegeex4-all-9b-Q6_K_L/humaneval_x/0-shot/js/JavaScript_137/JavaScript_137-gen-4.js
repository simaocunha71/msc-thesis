```js
const compareOne = (a, b) => {
  const na = Number(a)
  const nb = Number(b)
  if (na == nb) return null
  return na > nb ? a : b
}
```
