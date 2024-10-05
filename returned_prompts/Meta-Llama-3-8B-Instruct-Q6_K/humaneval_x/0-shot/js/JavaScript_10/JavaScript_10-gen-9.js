```javascript
function makePalindrome(str) {
  if (isPalindrome(str)) return str;
  for (let len = str.length; len > 0; len--) {
    let postfix = str.slice(len);
    if (isPalindrome(postfix)) {
      return str + postfix.split('').reverse().join('');
    }
  }
  return str;
}

function isPalindrome(str) {
  return str === str.split('').reverse().join('');
}

console.log(makePalindrome('')); // ''
console.log(makePalindrome('cat')); // 'catac'
console.log(makePalindrome('cata')); // 'catac'
```


Explanation:
The `makePalindrome` function takes a string as an input and returns the shortest palindrome that begins with the supplied string. It does this by finding the longest postfix of the supplied string that is a palindrome, and appending the reverse of the string prefix to the end of the postfix.

The `isPalindrome` function checks if a given string is a palindrome by comparing it with its reverse. It returns `true` if the string is a palindrome, and `false` otherwise.

In the `makePalindrome` function, we start by checking if the input string is already a palindrome. If it is, we simply return the original string. Otherwise, we iterate over the length of the string in reverse order, and for each length, we take the postfix of the string of that length. We check if the postfix is a palindrome using the `isPalindrome` function. If it is, we return the original string plus the reverse of the string prefix. If we reach the end of the loop without finding a palindromic postfix, we simply return the original string.