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
  const isEvenPalindrome = (x) => x % 2 === 0 ? true : false;
  const isOddPalindrome = (x) => x % 2 === 1 ? true : false;

  if (!(n >= 3 && n <= 100)) {
    throw new Error(`Input value of n is out of bounds. Expected to be [3, 99] but got ${n}`);
  }

  const result = [];

  for (let x = 1; x < n + 1; x++) {
    const currentPalindrome = evenOddPalindromes(x).filter((even) => isEvenPalindrome(even))
      .concat(oddOddPalindromes(x).filter((odd) => isOddPalindrome(odd)));
    result.push(...currentPalindrome);
  }

  return result;
};

const evenOddPalindromes = (n) => {
  const palindromes = [];
  for (let x = 1; x <= n + 1; x++) {
    if ((x % 2 === 0