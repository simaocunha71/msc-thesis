```java
const sortArray = (arr) => {
  arr.sort((a, b) => {
    let nA = a.toString(2).split('1').length - 1;
    let nB = b.toString(2).split('1').length - 1;
    if (nA === nB) {
      return a - b;
    }
    return nA - nB;
  });
  return arr;
}
```
