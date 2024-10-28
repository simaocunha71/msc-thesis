/*You will be given the name of a class (a string) and a list of extensions.
  The extensions are to be used to load additional classes to the class. The
  strength of the extension is as follows: Let CAP be the number of the uppercase
  letters in the extension's name, and let SM be the number of lowercase
  letters in the extension's name, the strength is given by the fraction CAP - SM.
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
  let strongest_extension = ''
  let strongest_strength = -1

  extensions.forEach(extension => {
    const extension_name = extension.split('.')[1]
    const strength = extension_name.match(/[A-Z]/g).length - extension_name.match(/[a-z]/g).length

    if (strength > strongest_strength) {
      strongest_strength = strength
      strongest_extension = extension
    }
  })

  if (strongest_extension === '') {
    return `${class_name}.${extensions[0]}`
  }

  return `${class_name}.${strongest_extension.split('.')[1]}`
}

