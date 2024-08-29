  const isPalindrome = (num) => {
    const str = num.toString();
    for (let i = 0; i < Math.floor(str.length / 2); i++) {
      if (str.charAt(i) !== str.charAt(str.length - 1 - i)) {
        return false;
      }
    }
    return true;
  };

  let even_count = 0;
  let odd_count = 0;

  for (let i = 1; i <= n; i++) {
    if (isPalindrome(i)) {
      if (i % 2 === 0) {
        even_count += 1;
      } else {
        odd_count += 1;
      }
    }
  }

  return [even_count, odd_count];
}



