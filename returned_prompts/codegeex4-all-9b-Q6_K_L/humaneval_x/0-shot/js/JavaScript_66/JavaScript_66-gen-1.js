```java
const digitSum = (s) => {
  return s.split('').reduce((prev, item) => {
    if (item.toUpperCase() === item)
      return prev + item.charCodeAt(0);
    return prev;
  }, 0);
}
```
