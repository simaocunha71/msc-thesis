```java
const hexKey = (num) => {
  let t = 0
  for (let i = 0; i < num.length; i++) {
    if (num[i] == '2' || num[i] == '3' || num[i] == '5' || num[i] == '7' || num[i] == 'B' || num[i] == 'D') { t++ }
  }
  return t
}
```
