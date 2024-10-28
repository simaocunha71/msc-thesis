  var count = 0;

  for (var i = 0; i < s.length; i = i + 2) {
    if (s[i].toUpperCase() == s[i]) {
      count += 1;
    }
  }

  return count;
}



