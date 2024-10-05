Here is a JavaScript solution for the problem:

```javascript
const strongestExtension = (class_name, extensions) => {
  let strongest = null;
  let maxStrength = -Infinity;

  for (let extension of extensions) {
    let cap = 0;
    let sm = 0;
    for (let char of extension) {
      if (char === char.toUpperCase()) {
        cap++;
      } else {
        sm++;
      }
    }
    let strength = cap - sm;
    if (strength > maxStrength) {
      maxStrength = strength;
      strongest = extension;
    }
  }
  return `${class_name}.${strongest}`;
}
```
This function iterates over the list of extensions. For each extension, it counts the number of uppercase and lowercase letters and calculates the strength. If the strength of the current extension is greater than the maximum strength found so far, it updates the maximum strength and the strongest extension. Finally, it returns the class name followed by the strongest extension.

For example, if you call `strongestExtension('my_class', ['AA', 'Be', 'CC'])`, it will return `'my_class.AA'`.