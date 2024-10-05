Here is the solution in JavaScript:

```javascript
const strongestExtension = (class_name, extensions) => {
  let strongest = null;
  let maxStrength = -Infinity;

  for (let extension of extensions) {
    let cap = 0;
    let sm = 0;

    for (let char of extension) {
      if (char.toUpperCase() === char) {
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

  return class_name + '.' + strongest;
};
```

This function iterates over each extension, calculates its strength, and keeps track of the strongest extension seen so far. If a stronger extension is found, it updates the strongest extension. Finally, it returns the class name followed by the strongest extension. If there are multiple extensions with the same strength, it returns the one that comes first in the list.

You can test this function with the example you provided:

```javascript
console.log(strongestExtension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])); // Output: 'Slices.SErviNGSliCes'
``` 