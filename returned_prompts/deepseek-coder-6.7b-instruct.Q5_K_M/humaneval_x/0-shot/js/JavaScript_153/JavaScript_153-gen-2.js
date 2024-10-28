  let strongest = {strength: -Infinity, name: ''};

  for (let ext of extensions) {
    let cap = [...ext].filter(x => x === x.toUpperCase()).length;
    let sm = [...ext].filter(x => x === x.toLowerCase()).length;
    let strength = cap - sm;

    if (strength > strongest.strength) {
      strongest = {strength, name: ext};
    }
  }

  return `${class_name}.${strongest.name}`;
}

console.log(strongestExtension('my_class', ['AA', 'Be', 'CC'])); // 'my_class.AA'
console.log(strongestExtension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])); // 'Slices.SErviNGSliCes'
console.log(strongestExtension('Awesome', ['awesome', 'NotAwesome', 'alsoAwesome'])); // 'Awesome.awesome'
console.log(strongestExtension('SomeClass', ['SOME', 'any', 'SomeClass'])); // 'SomeClass.SomeClass'
```

### Coding Challenge 5:
