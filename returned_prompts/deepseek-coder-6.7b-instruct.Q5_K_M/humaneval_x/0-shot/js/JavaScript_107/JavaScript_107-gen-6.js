
}

evenOddPalindrome(3);
evenOddPalindrome(12);

*/

const evenOddPalindrome = (n) => {
  const isPalindrome = (num) => {
    let strNum = num.toString();
    let len = strNum.length;
    for (let i = 0; i < len / 2; i++) {
      if (strNum[i] !== strNum[len - 1 - i]) return false;
    }
    return true;
  };

  let even = 0,
    odd = 0;
  for (let i = 1; i <= n; i++) {
    if (isPalindrome(i)) {
      if (i % 2 === 0) even++;
      else odd++;
    }
  }
  return [even, odd];
};

console.log(evenOddPalindrome(3)); // [1, 2]
console.log(evenOddPalindrome(12)); // [4, 6]

// Time complexity: O(n * k), where k is the number of digits in n.
// Space complexity: O(1), since we're using a constant amount of space.

// To improve the efficiency we can use a precomputed table to store the palindrome results up to n.
// But, since we're using JavaScript, it has a limit on the maximum size of the array that can be created.
// So, for n <= 10^3, the above solution will work fine.

// This solution could be improved using memoization to avoid re-computation of palindrome numbers.
// But since JavaScript has a limit on the maximum size of the array that can be created,
// for n <= 10^3, the above solution will work fine.

// Time complexity: O(n), where n is the input number.
// Space complexity: O(1), since we're using a constant amount of space.

// This solution could also be improved by using multi-threading or parallel processing to check for palindrome numbers,
// but this would require a more complex implementation and may not be worth it for such a small