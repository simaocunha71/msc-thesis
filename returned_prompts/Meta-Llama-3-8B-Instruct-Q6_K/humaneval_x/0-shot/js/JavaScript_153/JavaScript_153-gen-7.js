Here is the solution for the problem:

```javascript
const strongestExtension = (class_name, extensions) => {
  let strongest = null;
  let maxStrength = 0;

  for (let extension of extensions) {
    let cap = 0;
    let sm = 0;

    for (let char of extension) {
      if (char.match(/[A-Z]/)) {
        cap++;
      } else if (char.match(/[a-z]/)) {
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
};
```

You can call this function with a class name and a list of extensions as arguments, and it will return the class name with the strongest extension. The strongest extension is determined by the number of uppercase letters minus the number of lowercase letters in the extension's name. If there are multiple extensions with the same strength, it will choose the one that comes first in the list. For example:

```javascript
console.log(strongestExtension('my_class', ['AA', 'Be', 'CC'])); // Output: 'my_class.AA'
``` 