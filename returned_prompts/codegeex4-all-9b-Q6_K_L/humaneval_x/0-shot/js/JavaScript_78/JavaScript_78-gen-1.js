```java
const hexKey = (num) => {
  let s = 0
  for (let i = 0; i < num.length; i++) {
    if (num[i] == 'B' || num[i] == 'D' || num[i] == '2' || num[i] == '3' || num[i] == '5' || num[i] == '7') { s++ }
  }
  return s
}
```
