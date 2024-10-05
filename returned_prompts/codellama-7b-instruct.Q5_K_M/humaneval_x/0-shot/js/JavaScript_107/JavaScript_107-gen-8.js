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

    const palindromes = [];
    const isEven = num => num % 2 === 0;
    let num = 1;
    while (num < n) {
        palindromes.push(num);
        palindromes.push(num.toString().split('').reverse().join(''));
        if (isEven(num)) {
            num++;
        } else {
            num++;
        }
    }
    return palindromes.filter(isEven).length;
}

const evenOddPalindrome = (n) => {
    let even = 0;
    let odd = 0;
    for (let i = 1; i < n; i++) {
        const str = i.toString();
        if (str === str.split('').reverse().join('')) {
            if (i % 2 === 0) {
                even++;
            } else {
                odd++;
            }
        }
    }
    return [even, odd];
}

const evenOddPalindrome = (n) => {
    let even = 0;
    let odd = 0;