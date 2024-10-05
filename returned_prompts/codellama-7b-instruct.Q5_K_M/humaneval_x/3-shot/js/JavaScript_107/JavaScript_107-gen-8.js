  var even = 0;
  var odd = 0;

  for (var i = 1; i < n; i++) {
    if (isPalindrome(i)) {
      if (i % 2 == 0) {
        even++;
      } else {
        odd++;
      }
    }
  }

  return [even, odd];
}



