```java
const strongestExtension = (class_name, extensions) => {
  let max_str = -Infinity
  let max_str_ind = -1
  for (let i = 0; i < extensions.length; i++) {
    let ext = extensions[i]
    let cap = 0
    let sm = 0
    for (let j = 0; j < ext.length; j++) {
      if (ext[j] >= 'A' && ext[j] <= 'Z') {
        cap++
      } else if (ext[j] >= 'a' && ext[j] <= 'z') {
        sm++
      }
    }
    if (cap - sm > max_str) {
      max_str = cap - sm
      max_str_ind = i
    }
  }
  return `${class_name}.${extensions[max_str_ind]}`
}
```
