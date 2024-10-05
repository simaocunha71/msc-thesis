  let evenPalindromeCount = 0;
  let oddPalindromeCount = 0;

  for (let i = 1; i <= n; i++) {
    let str = i.toString();
    if (str === str.split('').reverse().join('')) {
      if (i % 2 === 0) {
        evenPalindromeCount++;
      } else {
        oddPalindromeCount++;
      }
    }
  }

  return [evenPalindromeCount, oddPalindromeCount];
}