```js
const isNested = (string) => {
  let stack = []
  for (let i = 0; i < string.length; i++) {
    if (string[i] === '[') {
      stack.push(1)
    } else {
      if (stack.length > 0) {
        stack.pop()
        if (stack.length > 0) {
          return true
        }
      }
    }
  }
  return false
}
```
