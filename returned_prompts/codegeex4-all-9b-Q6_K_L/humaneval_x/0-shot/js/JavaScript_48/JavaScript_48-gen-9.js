```js
const isPalindrome = (text) => {
  if (text.length === 0) return true;
  if (text.length === 1) return true;
  if (text[0] !== text[text.length - 1]) return false;
  return isPalindrome(text.slice(1, -1));
}
```