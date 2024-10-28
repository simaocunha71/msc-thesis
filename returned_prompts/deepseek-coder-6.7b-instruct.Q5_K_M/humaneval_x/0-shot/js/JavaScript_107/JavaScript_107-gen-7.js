  const isPalindrome = (n) => {
    return n.toString() === n.toString().split('').reverse().join('');
  }

  let evenCount = 0, oddCount = 0;

  for(let i=1; i<=n; i++){
    if(isPalindrome(i)){
      if(i % 2 === 0) evenCount++;
      else oddCount++;
    }
  }

  return [evenCount, oddCount];
}

evenOddPalindrome(3); // [1, 2]
evenOddPalindrome(12); // [4, 6]
```

## 01. 2D Array to 1D Array

