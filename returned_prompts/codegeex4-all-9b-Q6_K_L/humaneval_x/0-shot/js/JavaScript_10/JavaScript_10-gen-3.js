```js
const isPalindrome = (string) => {
  return string == string.split('').reverse().join('');
}

const makePalindrome = (string) => {
  if (string.length === 0) return '';
  if (isPalindrome(string)) return string;

  let i = 0;
  while (!isPalindrome(string.substring(i))) {
    i++;
  }
  return string + string.substring(0, i).split('').reverse().join('');
}

console.log(makePalindrome('')); // ''
console.log(makePalindrome('cat')); // 'catac'
console.log(makePalindrome('cata')); // 'catac'
```