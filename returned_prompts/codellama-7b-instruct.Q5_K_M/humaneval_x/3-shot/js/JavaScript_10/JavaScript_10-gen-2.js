  var palindrome = string;
  var postfix = '';
  var prefix = '';
  var max_postfix_length = string.length;

  for (var i = 0; i < max_postfix_length; i++) {
    var postfix = string.substring(string.length - i);
    if (isPalindrome(postfix)) {
      break;
    }
  }

  for (var i = 1; i <= postfix.length / 2; i++) {
    var prefix = string.substring(0, string.length - i);
    if (isPalindrome(prefix)) {
      break;
    }
  }

  return prefix + postfix.split('').reverse().join('');
}



