  var count = 0;
  for (var i = 0; i < n; i++) {
    for (var j = i + 1; j < n; j++) {
      for (var k = j + 1; k < n; k++) {
        if (i * i - i + 1 + j * j - j + 1 + k * k - k + 1 % 3 == 0) {
          count++;
        }
      }
    }
  }
  return count;
}



