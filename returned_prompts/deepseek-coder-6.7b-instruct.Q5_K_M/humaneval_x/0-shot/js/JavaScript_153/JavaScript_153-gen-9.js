  let strongest = [0, class_name + '.' + extensions[0]];
  for (let extension of extensions) {
    let cap = Array.from(extension).filter(x => x === x.toUpperCase()).length;
    let sm = Array.from(extension).filter(x => x === x.toLowerCase()).length;
    let strength = cap - sm;
    if (strength > strongest[0]) {
      strongest = [strength, class_name + '.' + extension];
    }
  }
  return strongest[1];
}

console.log(strongestExtension('my_class',  ['AA', 'Be', 'CC']));
console.log(strongestExtension('Slices',  ['SErviNGSliCes', 'Cheese', 'StuFfed']));




/*
Explaination:
We initialize the strongest array with the strength and name of the extension. We then iterate over the extensions array. For each extension, we calculate the strength by counting the number of uppercase and lowercase letters. We then compare this strength to the current strongest extension. If the new extension is stronger (has a higher strength), we update the strongest array. Finally, we return the name of the strongest extension.
*/

/*
Test the function with the following test cases:
1. strongestExtension('my_class',  ['AA', 'Be', 'CC'])  should return 'my_class.AA'
2. strongestExtension('Slices',  ['SErviNGSliCes', 'Cheese', 'StuFfed'])  should return 'Slices.SErviNGSliCes'
*/

/*
The output of the test cases should be:
1. 'my_class.AA'
2. 'Slices.SErviNGSliCes'
*/


*/
















































































