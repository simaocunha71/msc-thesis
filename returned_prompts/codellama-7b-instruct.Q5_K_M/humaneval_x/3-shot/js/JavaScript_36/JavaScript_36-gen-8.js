  var count = 0;
  for (var i = 0; i < n; i++) {
    if (i % 11 == 0 || i % 13 == 0) {
      if (i % 10 == 7) {
        count += 1;
      }
    }
  }
  return count;
}



