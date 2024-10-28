  var count = 0;

  for (var i = 0; i < s.length; i++) {
    if (i % 2 == 0) {
      if (s[i].toUpperCase() == s[i]) {
        count += 1;
      }
    }
  }

  return count;
}



