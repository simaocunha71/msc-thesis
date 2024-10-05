  const map = new Map([
    [1000, 'm'],
    [900, 'cm'],
    [500, 'd'],
    [400, 'cd'],
    [100, 'c'],
    [90, 'xc'],
    [50, 'l'],
    [40, 'xl'],
    [10, 'x'],
    [9, 'ix'],
    [5, 'v'],
    [4, 'iv'],
    [1, 'i']
  ]);

  let roman = '';

  for (const [decimal, romanNumeral] of map.entries()) {
    while (number >= decimal) {
      roman += romanNumeral;
      number -= decimal;
    }
  }

  return roman;
};

intToMiniRoman(19); // 'xix'
intToMiniRoman(152); // 'clii'
intToMiniRoman(426); // 'cdxxvi'

module.exports = intToMiniRoman;

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact

[Github](https://github.com/felipedantasr)

[LinkedIn](https://www.linkedin.com/in/felipedantasr/)

[Twitter](https://twitter.com/felipedantasr)

[Email](mailto:felipedantasr@gmail.com)

## Acknowledgments

I would like to thank [Mozilla Developer Network](https://developer.mozilla.org/en-US/) for the guide on how to create a roman numeral converter.

I would also like to thank [FreeCodeCamp](https://www.freecodecamp.org/) for the inspiration and resources to build this project.

Lastly, I would like to thank [Stack Overflow](https://stackoverflow.com