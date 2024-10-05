```java
const allPrefixes = (string) => {
  return Array.from({length: string.length}, (_, i) => string.slice(0, i + 1));
}
```