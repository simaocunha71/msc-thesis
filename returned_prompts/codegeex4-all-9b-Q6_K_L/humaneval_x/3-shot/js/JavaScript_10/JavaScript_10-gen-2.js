  if (isPalindrome(string)) {
    return string;
  }

  let longest_palindrome_suffix = '';
  for (let i = string.length; i > 0; i--) {
    let suffix = string.slice(string.length - i);
    if (isPalindrome(suffix)) {
      longest_palindrome_suffix = suffix;
      break;
    }
  }

  let prefix = string.slice(0, string.length - longest_palindrome_suffix.length);
  return string + prefix.split('').reverse().join('');
}



