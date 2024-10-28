  const isPalindrome = (num) => {
    let str = String(num);
    let reversed = str.split('').reverse().join('');
    return str === reversed;
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



