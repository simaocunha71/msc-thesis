```java
const uniqueDigits = (x) => {
  let result = x.filter(num => {
    let str = num.toString();
    for (let i = 0; i < str.length; i++) {
      if (str[i] % 2 === 0) {
        return false;
      }
    }
    return true;
  });
  return result.sort((a, b) => a - b);
}
```
