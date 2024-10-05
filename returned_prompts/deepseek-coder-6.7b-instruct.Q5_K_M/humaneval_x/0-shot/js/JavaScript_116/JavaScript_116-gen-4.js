  return arr.sort((a, b) => {
    let aBinary = a.toString(2);
    let bBinary = b.toString(2);
    let aOnes = aBinary.split('1').length - 1;
    let bOnes = bBinary.split('1').length - 1;

    return aOnes - bOnes || a - b;
  });
};

console.log(sortArray([1, 5, 2, 3, 4])); // [1, 2, 3, 4, 5]
console.log(sortArray([-2, -3, -4, -5, -6])); // [-6, -5, -4, -3, -2]
console.log(sortArray([1, 0, 2, 3, 4])); // [0, 1, 2, 3, 4]

```

## 2. Coin Combinations

Problem:
Given a number of cents, return the minimum number of coins that you would need to produce that value. 

You can use standard US denominations: `1¢`, `5¢`, `10¢`, `25¢`.

