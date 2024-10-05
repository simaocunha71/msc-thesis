```java
const getOddCollatz = (n) => {
  var arr = [];
  while (n > 1) {
    if (n % 2 === 1) arr.push(n);
    n = n % 2 === 0 ? n / 2 : n * 3 + 1;
  }
  arr.push(1);
  return arr.sort((a, b) => a - b);
}
```
The function works by creating an empty array `arr`, and then iteratively adding odd numbers to it from the Collatz sequence of `n`. The loop continues until `n` reaches 1, at which point 1 is added to the array. The array is then sorted in increasing order and returned.