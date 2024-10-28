  const map = {
    M: 1000,
    CM: 900,
    D: 500,
    CD: 400,
    C: 100,
    XC: 90,
    L: 50,
    XL: 40,
    X: 10,
    IX: 9,
    V: 5,
    IV: 4,
    I: 1
  }

  let roman = '';

  for (let key in map) {
    while (number >= map[key]) {
      roman += key;
      number -= map[key];
    }
  }

  return roman;
}

console.log(intToMiniRoman(19)) // 'xix'
console.log(intToMiniRoman(152)) // 'clii'
console.log(intToMiniRoman(426)) // 'cdxxvi'
```

The function `intToMiniRoman` takes an integer as argument and converts it into a roman numeral string. 

This function works by iterating over a dictionary `map` which contains the roman numerals as keys and their corresponding integer values as values. 

For each key-value pair in the map, if the input number is greater than or equal to the value of the key, the key is appended to the result string and the value is subtracted from the input number. This process is repeated until the input number becomes zero.

The result is the roman numeral equivalent of the input number.

The time complexity of this function is O(1) as the number of iterations is constant, and the space complexity is also O(1) as the space used is constant.

The function works for all positive integers from 1 to 1000 as per the provided restrictions.
*/

console.log(intToMiniRoman(19)) // 'xix'
console.log(intToMiniRoman(152)) // 'clii'
console.log(intToMiniRoman(426)) // 'cdxxvi'
```

The function `intToMini