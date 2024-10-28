```javascript
const isSimplePower = (x, n) => {
  if (x === 1) return true
  let power = 1
  while (power <= x) {
    if (power === x) return true
    power *= n
  }
  return false
}
```
