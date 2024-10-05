```js
const makePalindrome = (string) => {
  let i = 0
  for (i = 0; i < string.length; i++) {
    if (isPalindrome(string.slice(i))) break
  }
  return string + string.slice(0, i).split('').reverse().join('')
}

console.log(makePalindrome('')) // ''
console.log(makePalindrome('cat')) // 'catac'
console.log(makePalindrome('cata')) // 'catac'
```
