  var length = string.length;
  if (length == 0) {
    return '';
  }

  var start = 0;
  var end = length - 1;

  // Find the longest palindromic postfix
  while (start < end) {
    if (string[start] != string[end]) {
      return string + string.slice(0, start) + string.slice(end + 1);
    }
    start += 1;
    end -= 1;
  }

  return string + string[0];
}



