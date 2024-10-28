  var count = 0;

  for (let i = 1; i < n; i++) {
    if (i % 11 == 0 || i % 13 == 0) {
      var str = i.toString();
      for (let c of str) {
        if (c == '7') {
          count++;
        }
      }
    }
  }

  return count;
}