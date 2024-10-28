  var result_string = s.split('').filter(function (char) {
    if (!c.includes(char)) {
      return char;
    }
  }).join('');

  return [result_string, isPalindrome(result_string)];
}



