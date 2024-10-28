```java
const strongestExtension = (class_name, extensions) => {
  let max = Number.MIN_SAFE_INTEGER;
  let max_index = -1;
  let strength = 0;
  for (let i = 0; i < extensions.length; i++) {
    let CAP = 0;
    let SM = 0;
    for (let j = 0; j < extensions[i].length; j++) {
      if (extensions[i][j] === extensions[i][j].toUpperCase()) {
        CAP++;
      } else {
        SM++;
      }
    }
    strength = CAP - SM;
    if (strength > max) {
      max = strength;
      max_index = i;
    }
  }
  return class_name + '.' + extensions[max_index];
}
```
