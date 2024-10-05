/* Test if a given string is a palindrome. */
function isPalindrome(str) {
  return str.split('').reverse().join('') === str;
}

/* Find the shortest palindrome that begins with a supplied string. */
function makePalindrome(str) {
  let longestPostfix = '';
  let prefix = '';
  for (let i = 0; i < str.length; i++) {
    const substr = str.slice(i);
    if (isPalindrome(substr)) {
      longestPostfix = substr;
      break;
    }
  }
  for (let i = str.length - 1; i >= 0; i--) {
    const substr = str.slice(0, i + 1);
    if (isPalindrome(substr)) {
      prefix = substr;
      break;
    }
  }
  return str + prefix.split('').reverse().join('');
}
