  var even = 0, odd = 0;
  for (var i = 1; i < n; i++) {
    var num = i.toString();
    if (num == num.split('').reverse().join('')) {
      if (i % 2 == 0) {
        even++;
      } else {
        odd++;
      }
    }
  }

  return [even, odd];
}



