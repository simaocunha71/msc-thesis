  var result = '';
  for (var i = 0; i < s.length; i++) {
    if (c.indexOf(s[i]) == -1) {
      result += s[i];
    }
  }
  return [result, isPalindrome(result)];
}



