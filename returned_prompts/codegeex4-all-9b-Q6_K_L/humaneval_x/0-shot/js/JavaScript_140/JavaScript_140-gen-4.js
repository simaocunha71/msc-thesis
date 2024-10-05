```javascript
const fixSpaces = (text) => {
  const words = text.split(' ')
  let result = []
  for (let i = 0; i < words.length; i++) {
    if (words[i] === '') {
      result[result.length - 1] += '-'
    } else {
      result.push(words[i])
    }
  }
  return result.join('_')
}
```