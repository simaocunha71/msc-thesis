  let strongest = '';
  let max_strength = -Infinity;

  for (const extension of extensions) {
    let cap = 0;
    let sm = 0;
    for (const c of extension) {
      if (c.toUpperCase() === c) {
        cap++;
      } else {
        sm++;
      }
    }
    let strength = cap - sm;
    if (strength > max_strength) {
      max_strength = strength;
      strongest = extension;
    }
  }

  return class_name + '.' + strongest;
}
// Example usage:
console.log(strongestExtension('my_class', ['AA', 'Be', 'CC'])); // 'my_class.AA'
console.log(strongestExtension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])); // 'Slices.SErviNGSliCes'
console.log(strongestExtension('my_class', ['Aa', 'B', 'Cc'])); // 'my_class.Aa'
console.log(strongestExtension('my_class', ['Aa', 'Bb', 'Cc'])); // 'my_class.Aa' // because 'Aa' comes first in the list
console.log(strongestExtension('my_class', ['Aa', 'B', 'Cc', 'Aa'])); // 'my_class.Aa' // because 'Aa' comes first in the list
console.log(strongestExtension('my_class', ['Aa', 'B', 'Cc', 'Aa', 'Aa'])); // 'my_class.Aa' // because 'Aa' comes first in the list
console.log(strongestExtension('my_class', ['Aa', 'Bb', 'Cc', 'Aa', 'Aa', 'Aa'])); // 'my_class.Aa' // because 'Aa' comes first in the list
console.log(strongestExtension('my_class', ['Aa', 'Bb', 'Cc', 'Aa', 'Aa', 'Aa', 'Aa'])); // 'my_class.Aa' // because 'Aa' comes first in the list
console.log(strongestExtension('my_class', ['Aa', 'Aa', 'Bb', 'Cc'])); // 'my_class.Aa' // because 'Aa' comes first in the list
console.log(strongestExtension('my_class', ['Aa', 'Aa', '