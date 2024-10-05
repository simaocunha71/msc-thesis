```js
const selectWords = (s, n) => {
  if(s === '') return []
  let words = s.split(' ')
  let consonantRegex = /[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]/
  let result = []
  for(let i=0; i<words.length; i++) {
    let count = 0
    for(let j=0; j<words[i].length; j++) {
      if(consonantRegex.test(words[i][j])) count++
    }
    if(count === n) result.push(words[i])
  }
  return result
}
```
