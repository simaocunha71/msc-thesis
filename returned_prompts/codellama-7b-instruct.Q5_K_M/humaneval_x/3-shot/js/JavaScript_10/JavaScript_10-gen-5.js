  if (isPalindrome(string)) {
    return string;
  } else {
    var longest_suffix = '';
    var longest_prefix = '';

    for (let i = 0; i < string.length; i++) {
      var suffix = string.substring(i, string.length);
      if (isPalindrome(suffix)) {
        longest_suffix = suffix;
      }
    }

    for (let i = 0; i < string.length; i++) {
      var prefix = string.substring(0, i);
      if (isPalindrome(prefix)) {
        longest_prefix = prefix;
      }
    }

    return longest_prefix + longest_suffix.split('').reverse().join('');
  }
}



