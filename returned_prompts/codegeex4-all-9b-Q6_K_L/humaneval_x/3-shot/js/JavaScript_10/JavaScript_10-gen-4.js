  let palindrome_suffix = string.split('').reverse().join('');
  let prefix = string;
  for (let i = 0; i < string.length; i++) {
    prefix = prefix.slice(0, string.length - i);
    if (prefix == palindrome_suffix) {
      return string + string.slice(0, i).split('').reverse().join('');
    }
  }
}

/* Return the first palindromic substring of given string that starts after given index.
  >>> findPalindrome('racecar', 4)
  'racecar'
  >>> findPalindrome('racecar', 5)
  'aceca'
  */
const findPalindrome = (string, index) => {
  return string.slice(index).split('').reverse().join('');
}