```js
const isPalindrome = (string) => {
  return string == string.split('').reverse().join('');
}

const makePalindrome = (string) => {
  if (isPalindrome(string)) {
    return string;
  }
  for (let i = string.length - 1; i >= 0; i--) {
    let suffix = string.slice(i);
    if (isPalindrome(suffix)) {
      let prefix = string.slice(0, i);
      return string + prefix.split('').reverse().join('');
    }
  }
  return '';
}
```