  const symbolValues = [
    ["m", 1000], ["cm", 900], ["d", 500], ["cd", 400],
    ["c", 100], ["xc", 90], ["l", 50], ["xl", 40],
    ["x", 10], ["ix", 9], ["v", 5], ["iv", 4],
    ["i", 1]
  ];

  let roman = '';

  for (const [symbol, value] of symbolValues) {
    while (number >= value) {
      roman += symbol;
      number -= value;
    }
  }

  return roman;
};

module.exports = intToMiniRoman;
```

## Test

```javascript
const intToMiniRoman = require('./intToMiniRoman');

console.log(intToMiniRoman(19) === 'xix');
console.log(intToMiniRoman(152) === 'clii');
console.log(intToMiniRoman(426) === 'cdxxvi');
```

## Time Complexity

The time complexity of this solution is O(1) since the number of iterations does not change with the size of the input. We just iterate over a fixed number of symbols (13 in this case).

## Space Complexity

The space complexity of this solution is O(1) as well because we only use a constant amount of space to store the `symbolValues` array and the resulting `roman` string. The size of these data structures does not change with the size of the input.

## Improvement

The solution is already optimal for this problem, but if we needed to support larger numbers, we could consider a more efficient approach that uses a map to store the symbol-value pairs. This would involve creating the `symbolValues` array only once, at the start of the program. This approach would have a space complexity of O(1), but a slightly higher time complexity of O(n), where n is the number of symbol-value pairs.

## Note

This solution assumes that the input is a valid positive integer in the