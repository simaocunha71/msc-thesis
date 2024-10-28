```java
const matchParens = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    for (let j = 0; j < lst[i].length; j++) {
      if (lst[i][j] == '(') {
        sum += 1;
      } else {
        sum -= 1;
      }
    }
  }
  if (sum == 0) {
    return 'Yes';
  } else {
    return 'No';
  }
}
```
