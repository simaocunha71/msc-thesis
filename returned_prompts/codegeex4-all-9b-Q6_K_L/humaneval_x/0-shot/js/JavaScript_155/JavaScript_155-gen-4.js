```java
const evenOddCount = (num) => {
  if (num < 0) num = -num;
  let evens = 0;
  let odds = 0;
  while (num > 0) {
    let digit = num % 10;
    if (digit % 2 === 0) evens++;
    else odds++;
    num = Math.floor(num / 10);
  }
  return [evens, odds];
}
```
