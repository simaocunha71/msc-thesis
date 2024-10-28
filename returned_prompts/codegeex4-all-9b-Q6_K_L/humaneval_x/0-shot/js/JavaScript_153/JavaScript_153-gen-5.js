```java
const strongestExtension = (class_name, extensions) => {
  var max_strengh = -Infinity
  var max_extension = ''
  for (var extension of extensions) {
    var strength = 0
    for (var char of extension) {
      if (char == char.toUpperCase()) strength++
      else strength--
    }
    if (strength > max_strengh) {
      max_strengh = strength
      max_extension = extension
    }
  }
  return class_name + '.' + max_extension
}
```
