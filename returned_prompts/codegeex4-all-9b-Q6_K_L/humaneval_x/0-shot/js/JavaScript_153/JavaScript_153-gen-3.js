```java
const strongestExtension = (class_name, extensions) => {
  let max = -Infinity
  let idx = -1
  for (let i = 0; i < extensions.length; i++) {
    let cap = 0
    let sm = 0
    for (let j = 0; j < extensions[i].length; j++) {
      if (extensions[i][j] >= 'A' && extensions[i][j] <= 'Z') { cap++ }
      else if (extensions[i][j] >= 'a' && extensions[i][j] <= 'z') { sm++ }
    }
    let strength = cap - sm
    if (strength > max) {
      max = strength
      idx = i
    }
  }
  return class_name + '.' + extensions[idx]
}
```
