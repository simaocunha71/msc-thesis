  var even = 0;
  var odd = 0;
  for (var i = 1; i <= n; i++) {
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

const isPalindrome = (n) => {
  var str = n.toString();
  var reversed = str.split('').reverse().join('');
  return str == reversed;
}