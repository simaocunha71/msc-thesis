```java
const strongestExtension = (class_name, extensions) => {
  let max_strength = -Infinity
  let max_extension = ''
  for (const ext of extensions) {
    let strength = 0
    for (const c of ext) {
      if (c === c.toUpperCase()) strength++
      else strength--
    }
    if (strength > max_strength) {
      max_strength = strength
      max_extension = ext
    }
  }
  return class_name + '.' + max_extension
}
```
