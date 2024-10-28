Here is the solution in JavaScript:
```javascript
const strongestExtension = (class_name, extensions) => {
  let strongestExtension = '';
  let strongestStrength = -Infinity;
  for (let extension of extensions) {
    let cap = extension.split('').filter(c => c.toUpperCase() === c).length;
    let sm = extension.split('').filter(c => c.toLowerCase() === c).length;
    let strength = cap - sm;
    if (strength > strongestStrength) {
      strongestExtension = extension;
      strongestStrength = strength;
    }
  }
  return class_name + '.' + strongestExtension;
};
```
Here's an explanation of how the solution works:
1. We initialize `strongestExtension` to an empty string and `strongestStrength` to negative infinity.
2. We iterate over the list of extensions using a for...of loop.
3. For each extension, we calculate the number of uppercase letters (`cap`) and lowercase letters (`sm`) using the `split` method and the `filter` method.
4. We calculate the strength of the extension as the difference between `cap` and `sm`.
5. If the strength of the current extension is greater than `strongestStrength`, we update `strongestExtension` to the current extension and `strongestStrength` to the current strength.
6. Finally, we return the class name followed by the strongest extension.

You can test the function with the example you provided:
```javascript
console.log(strongestExtension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])); // Output: 'Slices.SErviNGSliCes'
```