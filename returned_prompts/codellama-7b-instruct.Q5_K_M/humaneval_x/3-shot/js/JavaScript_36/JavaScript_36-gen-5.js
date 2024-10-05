  var count = 0;

  for (var i = 2; i < n; i++) {
    if (i % 11 == 0 || i % 13 == 0) {
      var str = i.toString();
      if (str.includes('7')) {
        count++;
      }
    }
  }

  return count;
}



