  var count = 0;

  for (var i = 1; i < n; i++) {
    if (i % 11 == 0 || i % 13 == 0) {
      var s = i.toString();
      for (const c of s) {
        if (c == '7') {
          count += 1;
        }
      }
    }
  }

  return count;
}