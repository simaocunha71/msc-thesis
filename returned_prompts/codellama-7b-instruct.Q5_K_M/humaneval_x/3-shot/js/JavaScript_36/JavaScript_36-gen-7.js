  var count = 0;

  for (var i = 1; i < n; i++) {
    if (i % 11 == 0 || i % 13 == 0) {
      var digits = i.toString().split('');
      for (var j = 0; j < digits.length; j++) {
        if (digits[j] == '7') {
          count++;
        }
      }
    }
  }

  return count;
}



