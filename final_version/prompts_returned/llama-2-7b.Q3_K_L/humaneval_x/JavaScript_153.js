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
  const extension_lengths = extensions.map((extension) =>
    extension
      .split("")
      .filter(letter => ["A", "B", "C"]
        .includes(letter[0]))
      .length
  );
  const strongest_extension = extensions.reduce((max, extn) => {
    if (extension_lengths.includes(extn)) max = Math.min(...extension_lengths);
    return max;
  }, extension_lengths[0]);
  
  console.log('strongest_extension: ' + strongest_extension);
  for (let i = 0; i < extensions.length; ++i) {
    const extn = extensions[i];
    
    if (extensions[i] === class_name && strongest_extension === extension_lengths[i]) {
      return class_name + '.' + extn;
    } else if (strongest_extension ===