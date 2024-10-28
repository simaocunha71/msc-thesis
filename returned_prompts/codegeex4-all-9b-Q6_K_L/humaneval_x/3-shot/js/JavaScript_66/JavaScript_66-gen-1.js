  var sum = 0;
  for (var i = 0; i < s.length; i++) {
    if (s[i] == s[i].toUpperCase()) {
      sum += s.charCodeAt(i);
    }
  }
  return sum;
}

