```js
const isPalindrome = (string) => {
  return string === string.split('').reverse().join('');
}

const makePalindrome = (string) => {
  let postfix = string;
  while (!isPalindrome(postfix) && postfix.length > 0) {
    postfix = postfix.slice(1);
  }
  let prefix = string.slice(postfix.length);
  return string + prefix.split('').reverse().join('');
}
```