```java
const stringSequence = (n) => {
  let result = '';
  for (let i = 0; i <= n; i++) {
    result += i.toString();
    if (i !== n) result += ' ';
  }
  return result;
}
```