  var result = [0, 0];

  for (var i = 1; i <= n; i++) {
    var s = i.toString();
    var j = i;
    var k = 0;
    while (k < s.length) {
      if (s[k] != s[s.length - 1 - k]) {
        break;
      }
      k++;
    }
    if (k == s.length && s.length % 2 != 0) {
      result[0] += 1;
    } else if (k == s.length && s.length % 2 == 0) {
      result[1] += 1;
    } else if (k != s.length && s.length % 2 != 0) {
      result[1] += 1;
    } else if (k != s.length && s.length % 2 == 0) {
      result[0] += 1;
    }
  }

  return result;
}



