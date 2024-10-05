```js
const isPalindrome = (string) => {
  return string == string.split('').reverse().join('');
}

const makePalindrome = (string) => {
  if (isPalindrome(string)) return string;
  const len = string.length;
  for (let i = len - 1; i >= 0; i--) {
    const prefix = string.slice(0, i + 1);
    const postfix = string.slice(i + 1);
    if (isPalindrome(prefix)) {
      return postfix.split('').reverse().join('') + string;
    }
  }
}
```