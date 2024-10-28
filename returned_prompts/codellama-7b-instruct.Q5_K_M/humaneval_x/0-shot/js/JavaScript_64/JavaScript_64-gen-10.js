/*Write a function to check whether a given string is a palindrome or not.
  A palindrome is a string that reads the same backward as forward.

  Example:
  >>> isPalindrome("racecar")
  true
  >>> isPalindrome("level")
  false
  */
  const isPalindrome = (s) => {
  let temp = s.split("").reverse().join("");
  return temp == s;
  }

