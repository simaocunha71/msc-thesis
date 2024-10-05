  var count = 0;
  for (var i = 1; i < n; i++) {
    if (i % 11 == 0 || i % 13 == 0) {
      var str = i.toString();
      for (const c of str) {
        if (c == '7') {
          count += 1;
        }
      }
    }
  }
  return count;
}