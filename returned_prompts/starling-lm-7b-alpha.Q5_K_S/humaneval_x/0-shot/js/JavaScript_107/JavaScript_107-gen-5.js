
  function isPalindrome(number) {
    let str = number.toString();
    for (let i = 0; i < Math.floor(str.length / 2); i++) {
      if (str[i] !== str[str.length - 1 - i]) {
        return false;
      }
    }
    return true;
  }

  let result = [];
  for (let i = 1; i <= n; i++) {
    if (isPalindrome(i)) {
      if (i % 2 === 0) {
        result[0]++;
      } else {
        result[1]++;
      }
    }
  }
  return result;
};



/*
  Given a positive integer n, return a list that has the number of even and odd
  integer palindromes that fall within the range(1, n), inclusive.

  Example 1:

      Input: 3
      Output: [1, 2]
      Explanation:
      Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

  Example 2:

      Input: 12
      Output: [4, 6]
      Explanation:
      Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

  Note:
      1. 1 <= n <= 10^3
      2. returned list has the number of even and odd integer palindromes respectively.

  Time: O(n)
  Space: O(1)

*/

// optimized solution
const evenOddPalindrome = (n) => {
  let result = [0, 0];
  for (let i = 1; i <= n; i++) {
    let num = i.toString();
    if (num === num.split('').reverse().join('')) {
      if (i % 2 === 0) {
        result[0]++;
      } else