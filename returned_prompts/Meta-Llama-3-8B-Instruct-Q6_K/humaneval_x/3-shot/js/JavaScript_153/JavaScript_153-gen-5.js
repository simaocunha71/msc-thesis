  let strongest = { strength: 0, name: '' };
  for (const extension of extensions) {
    const cap = extension.toUpperCase().split('').filter(c => c === c.toUpperCase()).length;
    const sm = extension.toLowerCase().split('').filter(c => c === c.toLowerCase()).length;
    const strength = cap - sm;
    if (strength > strongest.strength) {
      strongest = { strength, name: extension };
    }
  }
  return class_name + '.' + strongest.name;
}
// Test:
console.log(strongestExtension('my_class', ['AA', 'Be', 'CC'])); // 'my_class.AA'
console.log(strongestExtension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])); // 'Slices.SErviNGSliCes'
console.log(strongestExtension('my_class', ['AA', 'bb', 'CC'])); // 'my_class.AA'
console.log(strongestExtension('my_class', ['AA', 'BB', 'CC'])); // 'my_class.AA'
console.log(strongestExtension('my_class', ['AA', 'BB', 'cc'])); // 'my_class.AA'
console.log(strongestExtension('my_class', ['Aa', 'BB', 'CC'])); // 'my_class.Aa'
console.log(strongestExtension('my_class', ['aA', 'BB', 'CC'])); // 'my_class.aA'
console.log(strongestExtension('my_class', ['AA', 'Bb', 'CC'])); // 'my_class.AA'
console.log(strongestExtension('my_class', ['AA', 'BB', 'cC'])); // 'my_class.AA'
console.log(strongestExtension('my_class', ['AA', 'BB', 'cc'])); // 'my_class.AA'
console.log(strongestExtension('my_class', ['AA', 'BB', 'CCC'])); // 'my_class.AA'