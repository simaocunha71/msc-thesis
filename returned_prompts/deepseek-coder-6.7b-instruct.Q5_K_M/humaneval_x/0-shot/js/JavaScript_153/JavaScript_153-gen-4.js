  let strongest = {name: '', strength: -Infinity};

  extensions.forEach(extension => {
    let strength = countUpperCase(extension) - countLowerCase(extension);
    if (strength > strongest.strength) {
      strongest = {name: extension, strength: strength};
    }
  });

  return `${class_name}.${strongest.name}`;
}

const countUpperCase = str => [...str].reduce((cnt, char) => cnt + (char === char.toUpperCase() ? 1 : 0), 0);
const countLowerCase = str => [...str].reduce((cnt, char) => cnt + (char === char.toLowerCase() ? 1 : 0), 0);

console.log(strongestExtension('my_class', ['AA', 'Be', 'CC'])); // my_class.AA
console.log(strongestExtension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])); // Slices.SErviNGSliCes
console.log(strongestExtension('my_class', ['aa', 'bB', 'cc'])); // my_class.bB


In the function `strongestExtension`, I create an object `strongest` to keep track of the strongest extension's name and strength. I then iterate over the list of extensions, calculate the strength of each extension, and if it is greater than the current strongest extension, I update `strongest`. Finally, I return the class name and the strongest extension's name concatenated by a dot. The helper functions `countUpperCase` and `countLowerCase` are used to count the number of uppercase and lowercase letters in a string respectively.
*/

/*
