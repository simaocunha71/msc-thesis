```java
const allPrefixes = (string) => {
  let prefix = [];
  for (let i = 0; i < string.length; i++) {
    prefix.push(string.slice(0, i + 1));
  }
  return prefix;
}
```