  if (!lst.length) return 0;
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (typeof lst[i] === 'number' && lst[i] > 0 && lst[i] % 2 !== 0) {
      sum += Math.pow(lst[i], 2);
    }
  }
  return sum;
}

console.log(doubleTheDifference([1, 3, 2, 0])); //10
console.log(doubleTheDifference([-1, -2, 0])); //0
console.log(doubleTheDifference([9, -2])); //81
console.log(doubleTheDifference([0])); //0
console.log(doubleTheDifference([])); //0

module.exports = doubleTheDifference;


```

## 2. Write a function called `sumOfOddElements` that takes an array as an argument and returns the sum of the odd elements in the array. If the array is empty or all elements are even, return 0.

```javascript
