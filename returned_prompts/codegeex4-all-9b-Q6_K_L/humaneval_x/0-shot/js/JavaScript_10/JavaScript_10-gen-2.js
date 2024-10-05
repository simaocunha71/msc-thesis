```js
const isPalindrome = (string) => {
  return string == string.split('').reverse().join('');
}

const makePalindrome = (string) => {
  let n = string.length;
  let i = n - 1;
  while (i >= 0 && !isPalindrome(string.substring(0, i + 1))) {
    i--;
  }
  return string + string.substring(0, n - i - 1).split('').reverse().join('');
}
```
