```java
const digitSum = (s) => {
  return s.split('').reduce((prev, char) => {
    if (char == char.toUpperCase() && isNaN(char)) {
      return prev + char.charCodeAt(0);
    }
    return prev;
  }, 0);
}
```
