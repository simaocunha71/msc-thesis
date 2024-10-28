  var result_string = "";
  for (const sc of s) {
    if (!c.includes(sc)) {
      result_string += sc;
    }
  }

  return [result_string, isPalindrome(result_string)];
}



