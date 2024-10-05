  var evenCount = 0;
  var oddCount = 0;
  for (var i = 1; i <= n; i++) {
    if (isPalindrome(i)) {
      if (i % 2 == 0) {
        evenCount += 1;
      } else {
        oddCount += 1;
      }
    }
  }
  return [evenCount, oddCount];
}

const isPalindrome = (n) => {
  var str = n.toString();
  var reversed = str.split('').reverse().join('');
  return str == reversed;
}