/*You will be given the name of a class (a string) and a list of extensions.
  The extensions are to be used to load additional classes to the class. The
  strength of the extension is as follows: Let CAP be the number of the uppercase
  letters in the extension's name, and let SM be the number of lowercase letters
  in the extension's name, the strength is given by the fraction CAP - SM.
  You should find the strongest extension and return a string in this
  format: ClassName.StrongestExtensionName.
  If there are two or more extensions with the same strength, you should
  choose the one that comes first in the list.
  For example, if you are given "Slices" as the class and a list of the
  extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
  return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension
  (its strength is -1).
  Example:
  for strongestExtension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
  */
const strongestExtension = (class_name, extensions) => {
  let strongest_extension = "";
  let highest_strength = 0;
  for (let i = 0; i < extensions.length; i++) {
    let current_strength = 0;
    for (let j = 0; j < extensions[i].length; j++) {
      if (extensions[i][j] === extensions[i][j].toUpperCase()) {
        current_strength++;
      } else {
        current_strength--;
      }
    }
    if (current_strength > highest_strength) {
      strongest_extension = extensions[i];
      highest_strength = current_strength;
    } else if (current_strength === highest_strength && i < extensions.length) {
      strongest_extension = extensions[i];
      highest_strength = current_strength;
    }
  }
  return class_name + "."