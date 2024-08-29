  var longest_palindrome_suffix = getLongestPalindromeSuffix(string);
  var reversed_prefix = getPrefix(string).slice(0, longest_palindrome_suffix.length);
  return string + reversed_prefix + longest_palindrome_suffix;
}

const getPrefix = (string) => {
  while (string.length > 0 && string[0] == string[string.length - 1]) {
    string = string.slice(1, -1);
  }
  return string;
}

const getLongestPalindromeSuffix = (string) => {
  var result = '';
  var current_result = '';
  for (let i = string.length - 1; i >= 0; i--) {
    current_result += string[i];
    if (isPalindrome(current_result)) {
      result = current_result;
    } else if (current_result.length > result.length) {
      result = current_result.slice(0, -1);
    }
  }
  return result;
}



