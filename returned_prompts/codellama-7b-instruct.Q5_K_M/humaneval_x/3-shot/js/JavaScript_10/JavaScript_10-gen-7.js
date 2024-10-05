  var palindromes = [string];
  var postfix = '';

  while (palindromes[palindromes.length - 1].length > 0) {
    postfix = palindromes.pop();
    var prefix = string.substring(0, string.length - postfix.length);
    var candidate = prefix + postfix;
    if (isPalindrome(candidate)) {
      return candidate;
    }
  }

  return string + reverse(string);
}



