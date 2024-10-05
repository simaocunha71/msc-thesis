  let maxStrength = -Infinity;
  let strongestExt = '';
  
  for (let ext of extensions) {
    let strength = ext.split('').reduce((acc, char) => {
      return char === char.toUpperCase() ? acc + 1 : acc - 1;
    }, 0);
    if (strength > maxStrength) {
      maxStrength = strength;
      strongestExt = ext;
    }
  }
  
  return `${class_name}.${strongestExt}`;
};

console.log(strongestExtension('my_class', ['AA', 'Be', 'CC']))
console.log(strongestExtension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))
```

### Solution:

The solution works by iterating over each extension and calculating its strength by counting the number of uppercase characters and subtracting the number of lowercase characters. The extension with the highest strength is considered the strongest. The function returns a string in the format 'ClassName.StrongestExtensionName'.

In the given example, the class is 'my_class' and the extensions are ['AA', 'Be', 'CC']. The 'AA' extension has the highest strength (1 - 2 = -1) so it is the strongest.

Similarly, in the second example, the class is 'Slices' and the extensions are ['SErviNGSliCes', 'Cheese', 'StuFfed']. The 'SErviNGSliCes' extension has the highest strength (1 - 11 = 10) so it is the strongest.

So, the function returns 'my_class.AA' and 'Slices.SErviNGSliCes' respectively.

The time complexity of this solution is O(n*m), where n is the number of extensions and m is the average length of the extension names. The space complexity is O(1) since no extra space is used that scales with the input size.

The code is written in JavaScript and uses the built-in reduce function to calculate the strength of each extension. The reduce function is called on each character in the extension name, and checks if