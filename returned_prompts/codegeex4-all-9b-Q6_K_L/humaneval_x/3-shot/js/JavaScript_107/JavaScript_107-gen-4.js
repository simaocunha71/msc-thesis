  var even = 0;
  var odd = 0;
  for (let i = 1; i <= n; i++) {
    if (isPalindrome(i)) {
      if (i % 2 == 0) {
        even += 1;
      } else {
        odd += 1;
      }
    }
  }

  return [even, odd];
}

const isPalindrome = (n) => {
  var original = n;
  var reversed = 0;
  while (n > 0) {
    let remainder = n % 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n / 10);
  }
  return original == reversed;
}

