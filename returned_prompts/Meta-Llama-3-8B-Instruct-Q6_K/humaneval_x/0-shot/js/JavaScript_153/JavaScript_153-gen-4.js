Here is a simple solution in JavaScript:
```javascript
const strongestExtension = (class_name, extensions) => {
  let strongest = { name: '', strength: -Infinity };
  for (const extension of extensions) {
    const cap = extension.replace(/[^A-Z]/g, '').length;
    const sm = extension.replace(/[^a-z]/g, '').length;
    const strength = cap - sm;
    if (strength > strongest.strength) {
      strongest = { name: extension, strength };
    }
  }
  return `${class_name}.${strongest.name}`;
};
```
Explanation:
We initialize a variable `strongest` to hold the strongest extension. We then iterate over each extension in the list. For each extension, we count the number of uppercase letters (`cap`) and lowercase letters (`sm`) using regular expressions. We calculate the strength of the extension as the difference between `cap` and `sm`. If the strength of the current extension is greater than the strength of the strongest extension found so far, we update `strongest`. Finally, we return the class name followed by the strongest extension name. If there are multiple extensions with the same strength, the one that comes first in the list will be chosen.