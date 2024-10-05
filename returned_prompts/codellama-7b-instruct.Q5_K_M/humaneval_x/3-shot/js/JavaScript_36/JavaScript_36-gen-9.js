  var count = 0;
  for (var i = 11; i < n; i++) {
    if (i % 11 == 0 || i % 13 == 0) {
      var str = i.toString();
      for (var j = 0; j < str.length; j++) {
        if (str[j] == '7') {
          count++;
        }
      }
    }
  }
  return count;
}



