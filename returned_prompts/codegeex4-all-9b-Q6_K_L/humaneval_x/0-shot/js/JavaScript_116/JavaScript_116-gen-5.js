```java
const sortArray = (arr) => {
  const countOnes = (num) => {
    let count = 0;
    while (num > 0) {
      count += num % 2;
      num = Math.floor(num / 2);
    }
    return count;
  }
  return arr.sort((a, b) => {
    const onesA = countOnes(a);
    const onesB = countOnes(b);
    if (onesA === onesB) {
      return a - b;
    } else {
      return onesA - onesB;
    }
  });
}
```
