  var count = 0;

  for (var i = 0; i < s.length; i++) {
    if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || (s[i] == 'y' && i == s.length - 1)) {
      count += 1;
    }
  }

  return count;
}



