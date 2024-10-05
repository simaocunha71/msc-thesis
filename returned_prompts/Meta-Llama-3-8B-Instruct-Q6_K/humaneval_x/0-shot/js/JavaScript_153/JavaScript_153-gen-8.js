Here is a possible solution in JavaScript:
```
const strongestExtension = (className, extensions) => {
  const strongest = { strength: -Infinity, extension: null };
  for (const extension of extensions) {
    const cap = extension.match(/[A-Z]/g).length;
    const sm = extension.match(/[a-z]/g).length;
    const strength = cap - sm;
    if (strength > strongest.strength) {
      strongest.strength = strength;
      strongest.extension = extension;
    }
  }
  return `${className}.${strongest.extension}`;
};
```
Here's an explanation of the code:

1. We initialize an object `strongest` with properties `strength` and `extension`, initialized to `-Infinity` and `null`, respectively. This object will keep track of the strongest extension found so far.
2. We iterate through the list of extensions using a `for...of` loop.
3. For each extension, we calculate the number of uppercase letters (`cap`) and lowercase letters (`sm`) using regular expressions.
4. We calculate the strength of the extension as `cap - sm`.
5. If the strength of the current extension is greater than the strength of the strongest extension found so far, we update the `strongest` object with the new strength and extension.
6. Finally, we return a string in the format `ClassName.StrongestExtensionName` using the `strongest` object.

You can test this function with the example you provided:
```
console.log(strongestExtension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])); // Output: "Slices.SErviNGSliCes"
```
Note that this implementation assumes that the extensions are strings. If the extensions can be of any type, you may need to modify the implementation accordingly.