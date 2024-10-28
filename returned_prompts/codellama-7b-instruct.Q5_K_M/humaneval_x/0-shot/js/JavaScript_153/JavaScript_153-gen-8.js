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
  const extensions_with_strength = extensions.map(extension => {
    const lowercase_count = extension.split('').filter(char => char.match(/^[a-z]+$/)).length
    const uppercase_count = extension.split('').filter(char => char.match(/^[A-Z]+$/)).length
    const strength = uppercase_count - lowercase_count
    return { extension, strength }
  })
  const strongest_extensions = extensions_with_strength.filter(extension => extension.strength === Math.max(...extensions_with_strength.map(extension => extension.strength)))
  const strongest_extension = strongest_extensions[0]
  return `${class_name}.${strongest_extension.extension}`
}

