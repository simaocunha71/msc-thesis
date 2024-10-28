  let strongest = [class_name, ""];
  let maxStrength = -Infinity;

  for (let ext of extensions) {
    let cap = (ext.match(/[A-Z]/g) || []).length;
    let sm = (ext.match(/[a-z]/g) || []).length;
    let strength = cap - sm;
    if (strength > maxStrength) {
      maxStrength = strength;
      strongest[1] = ext;
    }
  }

  return strongest.join(".");
}

console.log(strongestExtension("my_class", ['AA', 'Be', 'CC'])); // 'my_class.AA'
console.log(strongestExtension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'])); // 'Slices.SErviNGSliCes'
console.log(strongestExtension("Slices", ['se', 'a', 'bC', 'dEf'])); // 'Slices.bC'
console.log(strongestExtension("Class", ['c', 'B', 'A', 'd'])); // 'Class.d'

This function iterates over the given list of extensions and calculates the strength of each one by counting the number of uppercase and lowercase letters. The extension with the highest strength (i.e., the one with the largest difference between the number of uppercase and lowercase letters) is stored and returned along with the class name. If there are multiple extensions with the same strength, the one that comes first in the list is stored.

This solution assumes that the input class name and the list of extensions are non-empty and contain only alphanumeric characters and underscores. It also assumes that the class name and extension names are case-sensitive.
*/

//The function is case sensitive and it will return the first extension with the highest strength, if there are multiple extensions with the same strength.

let class_name = "my_class";
let extensions = ['AA', 'Be', 'CC'];
console.log(strongestExtension(class_name, extensions)); // 'my_class.AA'

class_name = "S