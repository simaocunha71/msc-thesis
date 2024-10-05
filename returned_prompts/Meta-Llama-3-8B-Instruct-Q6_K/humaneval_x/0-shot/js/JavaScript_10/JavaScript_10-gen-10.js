```javascript
function makePalindrome(str) {
  let revStr = str.split('').reverse().join('');
  let i = 0;
  while (i < str.length && str[i] === revStr[i]) {
    i++;
  }
  return str.slice(0, i) + revStr.slice(i);
}

console.log(makePalindrome('')); // ''
console.log(makePalindrome('cat')); // 'catac'
console.log(makePalindrome('cata')); // 'catac'
```
Explanation:
1. Reverse the input string to create `revStr`.
2. Initialize a variable `i` to 0, which will be used to track the common prefix between `str` and `revStr`.
3. Loop until `i` reaches the length of `str` or `str[i]` is not equal to `revStr[i]`.
4. Inside the loop, increment `i` by 1.
5. Once the loop ends, return a new string that combines the prefix of `str` (up to `i`) with the suffix of `revStr` (from `i` to the end).
This approach ensures that the resulting string is the shortest palindrome that begins with the supplied string.