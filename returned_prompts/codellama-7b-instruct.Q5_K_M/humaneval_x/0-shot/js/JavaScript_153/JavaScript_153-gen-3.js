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
  // Sort the extensions by their strength
  extensions.sort((a, b) => {
    const strengthA = a.toLowerCase().split('').filter(c => c >= 'a').length - a.toUpperCase().split('').filter(c => c >= 'A').length;
    const strengthB = b.toLowerCase().split('').filter(c => c >= 'a').length - b.toUpperCase().split('').filter(c => c >= 'A').length;
    return strengthA - strengthB;
  });

  // Get the strongest extension
  const strongest = extensions[0];

  return `${class_name}.${strongest}`;
}
