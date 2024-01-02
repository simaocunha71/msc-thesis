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
  */
const evenOddPalindrome = (n) => {
  let palindromes = [];
  for (let i = 0; i < n + 1; i++) {
    if (isEven(i)) {
      if (i % 2 === 0) palindromes.push(i);
    } else {
      if (i % 2 === 1) palindromes.push(i);
    }
  }
  return palindromes;
};

const isEven = (num) => {
  const firstPart = num / 2;
  const secondPart = Math.floor(num / 2);
  if ((firstPart + secondPart) % 2 === 0) return true;
  return false;
};