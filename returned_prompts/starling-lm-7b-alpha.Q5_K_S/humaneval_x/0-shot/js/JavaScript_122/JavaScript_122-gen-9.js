
let sum = 0;

for (let i = 0; i < k; i++) {
  if (arr[i].toString().length <= 2) {
    sum += arr[i];
  }
}
return sum;
};

console.log(addElements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4));






















B:
/*
  Given a string s, find the longest substring of length k (k is a positive integer) such that the longest substring composed of k characters is also a valid palindrome. If no such substring exists, return an empty string.

  Example 1:

  Input: s = "abcd", k = 2
  Output: "ab"
  Explanation: The longest substrings of length 2 are "ab", "bc", "cd". "ab" is the only palindrome, so we return "ab".

  Example 2:

  Input: s = "a", k = 1
  Output: "a"

  Example 3:

  Input: s = "banana", k = 3
  Output: "ana"


  Constraints:
      1. 1 <= len(s) <= 10^5
      2. 1 <= k <= 10^4

  Note:

  Given the string length and the value of k, it's possible that there are no valid substrings.

  In such case, you need to return an empty string ""

  */

function longestPalindrome(s, k) {
  let max = '';
  for (let i = 0; i < s.length - k + 1; i++) {
    let substr = s.substring(i, i + k);
    if (substr.length % 2 === 0 && substr === substr.split('').reverse().join('') ||
      substr.length % 2 === 1 && substr.split('').reverse().join('') === substr.slice(0, Math.floor