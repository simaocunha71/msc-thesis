  var result = '';
  for (let i = 0; i < s.length; i++) {
    if (i % 3 == 0) {
      result += s[i];
    } else {
      result = s[i] + result;
    }
  }
  return result;
}