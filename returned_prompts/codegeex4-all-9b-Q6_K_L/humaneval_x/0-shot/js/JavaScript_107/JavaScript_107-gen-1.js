```java
const evenOddPalindrome = (n) => {
  let even = 0, odd = 0;
  for (let i = 1; i <= n; i++) {
    if (i.toString() === i.toString().split("").reverse().join("")) {
      if (i % 2 === 0) {
        even++;
      } else {
        odd++;
      }
    }
  }
  return [even, odd];
}
```
