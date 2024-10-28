```js
const cycpatternCheck = (a, b) => {
  for(let i = 0; i < b.length; i++) {
    let rotated = b.slice(i) + b.slice(0, i)
    if(a.includes(rotated)) return true
  }
  return false
}
```