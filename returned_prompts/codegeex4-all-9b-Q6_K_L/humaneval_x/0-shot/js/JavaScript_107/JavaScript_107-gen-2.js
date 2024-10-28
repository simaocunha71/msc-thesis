```java
const evenOddPalindrome = (n) => {
  let even = 0;
  let odd = 0;
  for (let i = 1; i <= n; i++) {
    if (isPalindrome(i)) {
      if (i % 2 === 0) even++;
      else odd++;
    }
  }
  return [even, odd];
};

const isPalindrome = (num) => {
  let original = num;
  let reversed = 0;
  while (num > 0) {
    reversed = reversed * 10 + num % 10;
    num = Math.floor(num / 10);
  }
  return original === reversed;
}
```
