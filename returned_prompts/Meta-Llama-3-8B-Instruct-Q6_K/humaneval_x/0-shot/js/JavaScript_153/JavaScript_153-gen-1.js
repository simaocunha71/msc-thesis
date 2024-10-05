```javascript
const strongestExtension = (class_name, extensions) => {
  let strongest = null;
  let maxStrength = -Infinity;

  for (const extension of extensions) {
    const cap = extension.toUpperCase().split('').filter(c => c === c.toUpperCase()).length;
    const sm = extension.length - cap;
    const strength = cap - sm;

    if (strength > maxStrength) {
      maxStrength = strength;
      strongest = extension;
    }
  }

  return `${class_name}.${strongest}`;
};
```
The function `strongestExtension` takes two parameters: `class_name` and `extensions`. It iterates over the list of extensions, calculates the strength of each extension, and keeps track of the strongest extension found so far. If a stronger extension is found, it updates the strongest extension and the maximum strength. Finally, it returns the class name with the strongest extension.

For example, if you call `strongestExtension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])`, it will return `'Slices.SErviNGSliCes'`. If you call `strongestExtension('my_class', ['AA', 'Be', 'CC'])`, it will return `'my_class.AA'`.