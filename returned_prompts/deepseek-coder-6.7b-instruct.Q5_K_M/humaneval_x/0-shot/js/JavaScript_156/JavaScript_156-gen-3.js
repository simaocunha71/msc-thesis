  const roman = {
    1:    'i',
    4:    'iv',
    5:    'v',
    9:    'ix',
    10:   'x',
    40:   'xl',
    50:   'l',
    90:   'xc',
    100:  'c',
    400:  'cd',
    500:  'd',
    900:  'cm',
    1000: 'm'
  };

  let str = '';

  for (let i = 1000; i > 0; i = Math.floor(i / 10)) {
    while (number >= i) {
      str += roman[i];
      number -= i;
    }

    if (number >= 900 && number < 1000) {
      str += roman[100] + roman[1000];
      number -= 900;
    }

    if (number >= 400 && number < 500) {
      str += roman[100] + roman[500];
      number -= 400;
    }

    if (number >= 90 && number < 100) {
      str += roman[10] + roman[100];
      number -= 90;
    }

    if (number >= 40 && number < 50) {
      str += roman[10] + roman[50];
      number -= 40;
    }

    if (number >= 9 && number < 10) {
      str += roman[1] + roman[10];
      number -= 9;
    }

    if (number >= 4 && number < 5) {
      str += roman[1] + roman[5];
      number -= 4;
    }
  }

  return str.toLowerCase();
}

module.exports = intToMiniRoman;
```

## Testing

```js
console.log(intToMiniRoman(19) === 'xix');
console.log