```js
const isBored = (S) => {
  let boredom = 0
  let sentences = S.split(/\.|\?|!/).filter(x => x !== '')
  for (let i = 0; i < sentences.length; i++) {
    if (sentences[i].trim().startsWith('I')) {
      boredom++
    }
  }
  return boredom
}
```
