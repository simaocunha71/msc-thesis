```java
const hexKey = (num) => {
  let p = 0
  for (let i = 0; i < num.length; i++) {
    switch (num[i]) {
      case '2':
      case '3':
      case '5':
      case '7':
      case 'B':
      case 'D':
        p++
    }
  }
  return p
}
```
