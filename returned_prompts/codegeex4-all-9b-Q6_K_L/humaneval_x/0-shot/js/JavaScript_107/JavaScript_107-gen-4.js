```js
const isPalindrome = (num) => {
  const str = String(num);
  for (let i = 0; i < str.length / 2; i++) {
    if (str[i] !== str[str.length - 1 - i]) {
      return false;
    }
  }
  return true;
};

const evenOddPalindrome = (n) => {
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
};
```
