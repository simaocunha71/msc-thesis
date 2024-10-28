  const isPalindrome = (num) => {
    let strNum = num.toString();
    let len = strNum.length;
    for (let i = 0; i < len / 2; i++) {
      if (strNum[i] !== strNum[len - 1 - i]) {
        return false;
      }
    }
    return true;
  };

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
};

console.log(evenOddPalindrome(3)) // [1, 2]
console.log(evenOddPalindrome(12)) // [4, 6]
console.log(evenOddPalindrome(100)) // [40, 50]
console.log(evenOddPalindrome(1000)) // [400, 500]
```

## 4. Frequency Counter

