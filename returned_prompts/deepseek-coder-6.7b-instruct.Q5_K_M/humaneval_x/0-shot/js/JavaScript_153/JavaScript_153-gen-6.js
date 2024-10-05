  let maxStrength = -Infinity, strongest = '';

  for (let ext of extensions) {
    let cap = [...ext].filter(x => x === x.toUpperCase()).length;
    let sm = [...ext].filter(x => x === x.toLowerCase()).length;
    let strength = cap - sm;

    if (strength > maxStrength) {
      maxStrength = strength;
      strongest = ext;
    }
  }

  return `${class_name}.${strongest}`;
}

console.log(strongestExtension('my_class',  ['AA', 'Be', 'CC']));
// 'my_class.AA'
console.log(strongestExtension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']));
// 'Slices.SErviNGSliCes'
console.log(strongestExtension('SomeClass', ['aBc', 'DeFg', 'HiJk']));
// 'SomeClass.DeFg'
```

This function uses JavaScript array methods to get the count of uppercase and lowercase letters in the extension names. The difference between these counts is the strength of the extension, which is compared with maxStrength to find the strongest extension.

The function returns a string in the format 'ClassName.StrongestExtensionName' by concatenating the class name with the strongest extension name.
*/
---
title: "Haskell: Converting a list of tuples to a list of lists"
date: 2020-09-15T10:36:00+03:00
draft: false
tags: ['haskell']
categories: ['Haskell']
---

Haskell is a functional programming language, which means that it treats data as immutable and treats functions as first-class citizens. This means that you can manipulate data and functions as you would with any other data.

Let's say you have a list of tuples and you want to convert it to a list of lists in Haskell.

For example, if you have the list of tuples