```java
const evenOddPalindrome = (n) => {
  let even = 0, odd = 0
  for (let i = 1; i <= n; i++) {
    if (isPalindrome(i)) {
      if (i % 2 === 0) even++
      else odd++
    }
  }
  return [even, odd]
}

const isPalindrome = (num) => {
  let original = num, reverse = 0
  while (num > 0) {
    reverse = reverse * 10 + num % 10
    num = Math.floor(num / 10)
  }
  return original === reverse
}
```
