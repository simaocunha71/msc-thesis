```java
const strongestExtension = (class_name, extensions) => {
  var maxStrength = -Infinity
  var maxExt = ''
  for (const ext of extensions) {
    let strength = 0
    for (const c of ext) {
      if (c === c.toUpperCase()) strength++
      else strength--
    }
    if (strength > maxStrength) {
      maxStrength = strength
      maxExt = ext
    }
  }
  return class_name + '.' + maxExt
}
```
