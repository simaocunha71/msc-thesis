  var count = 0;
  for (var i = 0; i < n; i++) {
    if (i % 11 == 0 || i % 13 == 0) {
      var s = i.toString();
      for (var j = 0; j < s.length; j++) {
        if (s[j] == '7') {
          count += 1;
        }
      }
    }
  }
  return count;
}



