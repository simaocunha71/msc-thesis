  const isPalindrome = (num) => {
    return num.toString() === num.toString().split('').reverse().join('');
  }

  let evenCount = 0, oddCount = 0;

  for (let i = 1; i <= n; i++) {
    if (isPalindrome(i)) {
      if (i % 2 === 0) {
        evenCount++;
      } else {
        oddCount++;
      }
    }
  }

  return [evenCount, oddCount];
}



