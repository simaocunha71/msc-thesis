  var result = string;

  var palindromic_suffix = '';
  var palindromic_prefix = '';

  for (let i = string.length - 1; i >= 0; i--) {
    if (isPalindrome(string.substring(i))) {
      palindromic_suffix = string.substring(i);
      break;
    }
  }

  for (let j = 0; j < string.length; j++) {
    if (isPalindrome(string.substring(0, j))) {
      palindromic_prefix = string.substring(0, j);
      break;
    }
  }

  return palindromic_prefix + palindromic_suffix.split('').reverse().join('');
}


