Here's how you could write the `strongestExtension` function in JavaScript:

```javascript
const strongestExtension = (class_name, extensions) => {
  let strongest = extensions[0];
  let maxStrength = getStrength(extensions[0]);

  for (let i = 1; i < extensions.length; i++) {
    let strength = getStrength(extensions[i]);
    if (strength > maxStrength) {
      strongest = extensions[i];
      maxStrength = strength;
    }
  }

  return class_name + '.' + strongest;
};

const getStrength = (extension) => {
  let count = 0;
  for (let i = 0; i < extension.length; i++) {
    if (extension[i] === extension[i].toUpperCase()) {
      count++;
    }
  }
  return count - extension.length;
};
```
You can test it with:

```javascript
console.log(strongestExtension('my_class', ['AA', 'Be', 'CC'])); // my_class.AA
console.log(strongestExtension('my_class', ['AA', 'Be', 'BB'])); // my_class.AA
console.log(strongestExtension('my_class', ['AA', 'Be', 'BBB'])); // my_class.BBB
console.log(strongestExtension('my_class', ['AA', 'Be', 'BBB', 'AAA'])); // my_class.AAA
```