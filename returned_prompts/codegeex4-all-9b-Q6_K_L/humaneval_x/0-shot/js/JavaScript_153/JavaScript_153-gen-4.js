```java
const strongestExtension = (class_name, extensions) => {
  let best = extensions[0]
  for (let i = 1; i < extensions.length; i++) {
    if (extensions[i] > best) { best = extensions[i] }
  }
  return class_name + '.' + best
}
```
