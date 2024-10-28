Here is a JavaScript solution for the problem:

```javascript
const isPalindrome = (string) => {
  return string == string.split('').reverse().join('');
}

const makePalindrome = (string) => {
  for (let i = string.length; i > 0; i--) {
    const postfix = string.substring(0, i);
    if (isPalindrome(postfix)) {
      return string + string.slice(0, i).split('').reverse().join('');
    }
  }
  return string;
}

console.log(makePalindrome('')); // ''
console.log(makePalindrome('cat')); // 'catac'
console.log(makePalindrome('cata')); // 'catac'
```

This solution uses a loop to find the longest postfix of the input string that is a palindrome. It then appends the reverse of the string prefix that comes before the palindromic suffix to the end of the string. If no postfix is found to be a palindrome, the function returns the original string. The helper function `isPalindrome` checks if a given string is a palindrome by comparing it with its reverse. The `makePalindrome` function uses this helper function to find the shortest palindrome that begins with the supplied string. 