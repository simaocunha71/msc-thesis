Here is the solution using JavaScript:

```javascript
const strongestExtension = (class_name, extensions) => {
  let strongest = extensions[0];
  let strongestStrength = calculateStrength(extensions[0]);
  for (let i = 1; i < extensions.length; i++) {
    let extension = extensions[i];
    let extensionStrength = calculateStrength(extension);
    if (extensionStrength > strongestStrength) {
      strongest = extension;
      strongestStrength = extensionStrength;
    }
  }
  return class_name + '.' + strongest;
};

const calculateStrength = (extension) => {
  let cap = 0;
  let sm = 0;
  for (let i = 0; i < extension.length; i++) {
    if (extension[i] >= 'A' && extension[i] <= 'Z') {
      cap++;
    } else if (extension[i] >= 'a' && extension[i] <= 'z') {
      sm++;
    }
  }
  return cap - sm;
};
```

In this solution, we define a function `strongestExtension` that takes a class name and a list of extensions as arguments. It initializes the strongest extension as the first element in the list and calculates its strength. Then it iterates over the rest of the extensions, calculates their strengths, and updates the strongest extension if a stronger one is found. Finally, it returns the class name concatenated with the strongest extension.

The `calculateStrength` function is a helper function that calculates the strength of an extension. It counts the number of uppercase letters (CAP) and the number of lowercase letters (SM) in the extension, and returns the difference (CAP - SM) as the strength.

You can test the function with the example you provided:

```javascript
console.log(strongestExtension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])); // Output: 'Slices.SErviNGSliCes'
```