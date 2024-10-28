  var even = 0;
  var odd = 0;

  for (var i = 1; i <= n; i++) {
    var s = i.toString();
    if (s == s.split('').reverse().join('')) {
      if (i % 2 == 0) {
        even += 1;
      } else {
        odd += 1;
      }
    }
  }

  return [even, odd];
}