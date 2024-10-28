```js
const solve = (s) => {
  let ans = []
  let letters = false
  for (let i = 0; i < s.length; i++) {
    if (s[i].match(/[a-z]/i)) {
      letters = true
      if (s[i].match(/[A-Z]/)) ans.push(s[i].toLowerCase())
      else ans.push(s[i].toUpperCase())
    } else {
      ans.push(s[i])
    }
  }
  if (letters) return ans.join('')
  else return ans.reverse().join('')
}
```