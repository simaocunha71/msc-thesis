```java
const evenOddPalindrome = (n) => {
  let countOdd = 0;
  let countEven = 0;
  for (let i = 1; i <= n; i++) {
    if (isPalindrome(i)) {
      if (i % 2 == 0) {
        countEven++;
      } else {
        countOdd++;
      }
    }
  }
  return [countEven, countOdd];
}

const isPalindrome = (num) => {
  let str = num.toString();
  let reversedStr = str.split('').reverse().join('');
  return str === reversedStr;
}
```
