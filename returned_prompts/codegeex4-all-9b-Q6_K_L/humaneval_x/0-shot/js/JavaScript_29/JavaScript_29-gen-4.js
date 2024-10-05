```java
const filterByPrefix = (strings, prefix) => {
  if (!Array.isArray(strings)) {
    throw new Error("Expected first argument to be an array");
  }
  if (typeof prefix !== 'string') {
    throw new Error("Expected second argument to be a string");
  }
  return strings.filter(s => s.startsWith(prefix));
}
```