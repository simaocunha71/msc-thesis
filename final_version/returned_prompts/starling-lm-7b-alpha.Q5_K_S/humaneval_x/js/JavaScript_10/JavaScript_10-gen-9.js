  let longest_palindrome = getLongestPalindrome(string);
  let palindrome = string + longest_palindrome.slice(0, -1);
  return palindrome + palindrome.slice(0, longest_palindrome.length).split('').reverse().join('');
}

/* Find the longest palindrome that is a prefix of a string.
  It is possible to have multiple palindromes of same maximal length that are substrings of a string.
  This function returns only the first of them.
  >>> getLongestPalindrome('')
  ''
  >>> getLongestPalindrome('cat')
  ''
  >>> getLongestPalindrome('cata')
  'ata'
  >>> getLongestPalindrome('acbac')
  'acbac'
  */
const getLongestPalindrome = (string) => {
  let result = '';
  for (let i = string.length - 1; i >= 0; i--) {
    let left = i;
    let right = i;
    while (string[left] == string[right] && left >= 0 && right < string.length) {
      left--;
      right++;
    }
    if (right - left - 1 > result.length) {
      result = string.slice(left + 1, right);
    }
  }
  return result;
}



