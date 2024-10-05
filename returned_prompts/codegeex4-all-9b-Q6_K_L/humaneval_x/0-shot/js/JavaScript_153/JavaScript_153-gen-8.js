```java
const strongestExtension = (class_name, extensions) => {
  let strongest = extensions[0]
  for (let i = 1; i < extensions.length; i++) {
    let current = extensions[i]
    let strength1 = 0
    for (let j = 0; j < current.length; j++) {
      if (current[j] >= 'A' && current[j] <= 'Z') strength1++
    }
    let strength2 = current.length - strength1
    let strength3 = strength1 - strength2
    let strength4 = 0
    for (let j = 0; j < strongest.length; j++) {
      if (strongest[j] >= 'A' && strongest[j] <= 'Z') strength4++
    }
    let strength5 = strongest.length - strength4
    let strength6 = strength4 - strength5
    if (strength6 < strength3) strongest = current
  }
  return class_name + '.' + strongest
}
```
