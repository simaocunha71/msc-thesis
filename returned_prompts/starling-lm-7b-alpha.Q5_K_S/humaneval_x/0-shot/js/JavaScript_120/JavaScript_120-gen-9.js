    let sorted = arr.slice();
    sorted.sort((a, b) => b - a);

    return sorted.slice(0, k);
};

console.log(maximum([-3, -4, 5], 3)); // [-4, -3, 5]
console.log(maximum([4, -4, 4], 2)); // [4, 4]
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1)); // [2]

*/

/*
  Given a string s, find the longest palindromic substring in s. You can assume the
  input string contains only lowercase English alphabets.

  Example 

      Input: "babad"
      Output: "bab"
      Note: "bab" is a palindrome because "abba" is.

  Example 

      Input: "cbbd"
      Output: "bb"

  Example 

      Input: "a"
      Output: "a"

  Example 

      Input: ""
      Output: ""

  Note:

      The length of the input string s is between 1 and 1000.

  Hint:
      The length of a palindrome can be at most length of string/2

*/
const longestPalindrome = (s) => {
    let longest = '';
    for (let i = 0; i < s.length; i++) {
        let left = i;
        let right = i;
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        let len = right - left;
        if (len > longest.length) {
            longest = s.slice(left + 1, right);
        }
    }
    return longest;
};

console.log(longestPalindrome('babad')); // "bab"
console.log(longestPalindrome('cbbd')); // "bb"
console.log(longestPalindrome('a