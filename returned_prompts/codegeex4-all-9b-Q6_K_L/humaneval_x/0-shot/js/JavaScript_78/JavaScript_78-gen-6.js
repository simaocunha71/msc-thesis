```java
const hexKey = (num) => {
  const isPrime = (num) => [2, 3, 5, 7].includes(num);
  let count = 0;
  for (let i = 0; i < num.length; i++) {
    if (isPrime(parseInt(num[i], 16))) {
      count++;
    }
  }
  return count;
}
```
