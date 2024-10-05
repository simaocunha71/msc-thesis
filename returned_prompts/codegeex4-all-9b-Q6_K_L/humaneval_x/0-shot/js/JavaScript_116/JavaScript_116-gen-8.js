```java
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    let countA = a.toString(2).replace(/0/g, '').length;
    let countB = b.toString(2).replace(/0/g, '').length;
    if (countA === countB) {
      return a - b;
    } else {
      return countA - countB;
    }
  });
}
```
