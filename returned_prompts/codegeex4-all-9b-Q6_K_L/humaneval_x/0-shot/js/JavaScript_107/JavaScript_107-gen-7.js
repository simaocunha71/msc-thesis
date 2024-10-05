```java
const evenOddPalindrome = (n) => {
  var evens = 0, odds = 0;
  for (let i = 1; i <= n; i++) {
    if (isPalindrome(i)) {
      if (i % 2 == 0) {
        evens += 1;
      } else {
        odds += 1;
      }
    }
  }
  return [evens, odds];
}

const isPalindrome = (num) => {
  let str = String(num);
  let left = 0, right = str.length - 1;
  while (left < right) {
    if (str[left] != str[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
}
```
