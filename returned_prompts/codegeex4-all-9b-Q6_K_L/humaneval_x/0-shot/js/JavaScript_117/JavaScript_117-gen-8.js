```js
const selectWords = (s, n) => {
  let words = s.split(' ')
  let vowels = 'aeiou'
  let result = []
  for (let i = 0; i < words.length; i++) {
    let consonants = words[i].replace(/[aeiou]/gi, '')
    if (consonants.length === n) result.push(words[i])
  }
  return result
}
```
