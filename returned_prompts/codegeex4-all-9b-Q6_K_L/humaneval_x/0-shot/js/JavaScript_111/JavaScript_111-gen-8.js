```javascript
const histogram = (test) => {
  let count = {}
  let maxCount = 0
  let maxLetters = []
  test.split(' ').forEach((letter) => {
    if (count[letter]) {
      count[letter]++
    } else {
      count[letter] = 1
    }
    if (count[letter] > maxCount) {
      maxLetters = [letter]
      maxCount = count[letter]
    } else if (count[letter] === maxCount) {
      maxLetters.push(letter)
    }
  })
  return maxLetters.reduce((acc, letter) => {
    acc[letter] = maxCount
    return acc
  }, {})
}
```