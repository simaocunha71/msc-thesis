  if (isPalindrome(string)) {
    return string;
  }

  // Find the longest postfix of string that is a palindrome.
  for (let i = string.length; i >= 0; i--) {
    if (isPalindrome(string.slice(0, i))) {
      return string.slice(0, i) + string.slice(i).split('').reverse().join('');
    }
  }

  // If not found, append to the end of the string
  // reverse of a string prefix that comes before the palindromic suffix.
  let reverse = string.split('').reverse().join('');
  for (let i = 0; i < string.length; i++) {
    if (string[i] == reverse[i]) {
      return string.slice(0, i) + reverse.slice(i);
    }
  }
}



