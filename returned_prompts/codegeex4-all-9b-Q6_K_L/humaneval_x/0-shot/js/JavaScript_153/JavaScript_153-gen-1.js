```java
const strongestExtension = (class_name, extensions) => {
  let max = -Infinity
  let max_index = -1
  for (let i = 0; i < extensions.length; i++) {
    let strength = 0
    for (let j = 0; j < extensions[i].length; j++) {
      let c = extensions[i][j]
      if (c >= 'a' && c <= 'z') {
        strength -= 1
      } else if (c >= 'A' && c <= 'Z') {
        strength += 1
      }
    }
    if (strength > max) {
      max = strength
      max_index = i
    }
  }
  if (max_index == -1) {
    return class_name
  } else {
    return class_name + '.' + extensions[max_index]
  }
}
```
