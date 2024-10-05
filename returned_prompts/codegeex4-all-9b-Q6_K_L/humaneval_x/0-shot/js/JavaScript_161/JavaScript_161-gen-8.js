```js
const solve = (s) => {
  let letters = ''
  let nonLetters = ''
  for (let i = 0; i < s.length; i++) {
    if (/[a-zA-Z]/.test(s[i])) {
      letters += s[i].toUpperCase() === s[i] ? s[i].toLowerCase() : s[i].toUpperCase()
    } else {
      nonLetters += s[i]
    }
  }
  return letters.length ? letters + nonLetters.split('').reverse().join('') : nonLetters
}
```
