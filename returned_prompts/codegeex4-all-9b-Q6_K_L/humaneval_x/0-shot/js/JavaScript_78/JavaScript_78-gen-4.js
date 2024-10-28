```java
const hexKey = (num) => {
  let count = 0
  let hexa = ['2', '3', '5', '7', 'B', 'D']
  for (let i = 0; i < num.length; i++) {
    if (hexa.includes(num[i])) { count++ }
  }
  return count
}
```
