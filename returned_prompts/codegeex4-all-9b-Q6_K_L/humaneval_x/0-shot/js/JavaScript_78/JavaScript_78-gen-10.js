```java
const hexKey = (num) => {
  let prime = '2357BDF';
  let result = 0;
  for (let i = 0; i < num.length; i++) {
    if (prime.includes(num[i])) { result++ }
  }
  return result;
}
```
