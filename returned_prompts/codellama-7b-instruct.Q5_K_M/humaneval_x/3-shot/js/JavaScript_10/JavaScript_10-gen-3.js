  var palindrome = '';
  var prefix = '';
  var suffix = '';

  for (var i = string.length - 1; i >= 0; i--) {
    if (isPalindrome(string.slice(i))) {
      palindrome = string.slice(i);
      break;
    }
  }

  for (var j = string.length - 1; j >= 0; j--) {
    if (isPalindrome(string.slice(0, j + 1))) {
      prefix = string.slice(0, j + 1);
      break;
    }
  }

  return string + prefix.split('').reverse().join('') + palindrome;
}



