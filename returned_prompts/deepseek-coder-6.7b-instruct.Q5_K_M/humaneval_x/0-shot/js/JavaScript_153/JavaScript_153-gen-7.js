  let strongest = null;
  let maxStrength = -Infinity;
  
  for(let ext of extensions) {
    let strength = ext.split('').reduce((acc, char) => {
      if(char === char.toUpperCase() && isNaN(parseInt(char))) acc++;
      if(char === char.toLowerCase()) acc--;
      return acc;
    }, 0);
    
    if(strength > maxStrength) {
      maxStrength = strength;
      strongest = ext;
    }
  }
  
  return `${class_name}.${strongest}`;
};

console.log(strongestExtension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])); // "Slices.SErviNGSliCes"
console.log(strongestExtension('my_class', ['AA', 'Be', 'CC'])); // "my_class.AA"
console.log(strongestExtension('Test', ['aaa', 'BBB', 'ccc'])); // "Test.BBB"
console.log(strongestExtension('Class', ['AAA', 'bbb', 'CCC'])); // "Class.AAA"

// In this solution, we first initialize the `strongest` variable to `null` and `maxStrength` to `-Infinity`.
// Then we iterate over the `extensions` array. For each extension, we calculate its strength by splitting it into characters and reducing the array by adding 1 for each uppercase character and subtracting 1 for each lowercase character.
// We then check if this strength is greater than `maxStrength`. If it is, we update `maxStrength` and `strongest` to the current extension.
// Finally, we return a string in the format "ClassName.StrongestExtensionName" using the `class_name` and `strongest` variables.
// This solution assumes that the input will always be valid and that there will be at least one extension.
// Note: This solution assumes that the strength is the difference between the number of uppercase letters and lowercase letters in the extension's name. If the strength