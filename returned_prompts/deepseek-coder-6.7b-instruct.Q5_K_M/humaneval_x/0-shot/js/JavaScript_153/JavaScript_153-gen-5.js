  let maxStrength = Number.NEGATIVE_INFINITY;
  let strongestExtension = '';

  for (let ext of extensions) {
    let strength = ext.split('').reduce((acc, char) => {
      return char === char.toUpperCase() ? acc + 1 : acc - 1;
    }, 0);
    if (strength > maxStrength) {
      maxStrength = strength;
      strongestExtension = ext;
    }
  }

  return `${class_name}.${strongestExtension}`;
}

console.log(strongestExtension('my_class', ['AA', 'Be', 'CC'])); // 'my_class.AA'
console.log(strongestExtension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])); // 'Slices.SErviNGSliCes'
console.log(strongestExtension('another_class', ['aAa', 'bBb', 'cCc'])); // 'another_class.aAa'
```

## Credits

This problem was taken from the edabit platform.

## Contributors

- [@AakashR2](https://github.com/AakashR2)
- [@sharmaroshan](https://github.com/sharmaroshan)
- [@AryanKrGit](https://github.com/AryanKrGit)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used.
- Inspiration and problem solving.
- etc

---

# Problem 2

## Description

