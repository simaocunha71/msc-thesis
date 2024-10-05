/*
  Given a string, find the length of the longest substring without repeating characters.
  Example:
  Input: "abcabcbb"
  Output: 3
  Explanation: The answer is "abc", with the length of 3.
  Input: "bbbbb"
  Output: 1
  Explanation: The answer is "b", with the length of 1.
  Input: "pwwkew"
  Output: 3
  Explanation: The answer is "wke", with the length of 3.
  Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

[input/output] samples:
longestSubstring('abcabcbb') ==> 3
longestSubstring('bbbbb') ==> 1
longestSubstring('pwwkew') ==> 3
*/

const longestSubstring = (str) => {
  let longest = 0;
  let current = 0;
  let seen = {};

  for (let i = 0; i < str.length; i++) {
    if (str[i] in seen && seen[str[i]] >= 0) {
      longest = Math.max(longest, i - seen[str[i]]);
    } else {
      seen[str[i]] = i;
    }
  }
  longest = Math.max(longest, str.length - seen[str[str.length - 1]]);

  return longest;
};

module.exports = { intersection, longestSubstring };
