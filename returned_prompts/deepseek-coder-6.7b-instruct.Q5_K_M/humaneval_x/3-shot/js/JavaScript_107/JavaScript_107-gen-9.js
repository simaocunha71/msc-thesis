  const isPalindrome = (num) => {
    let reversed = parseInt(num.toString().split('').reverse().join(''));
    return num === reversed;
  }

  let evenCount = 0;
  let oddCount = 0;

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



