
};

// You can use the Math.ceil() function to round up a number.
// And the reduce() method can be used to iterate over each element of the array.
// Then, you can square each number and add it to the sum.

// Use this link to understand better: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/ceil
// Use this link to understand better: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce

```javascript
const sumSquares = (lst) => {
  return lst.reduce((sum, num) => {
    return sum + Math.pow(Math.ceil(num), 2);
  }, 0);
};
```


Test Cases:
```javascript
console.log(sumSquares([1,2,3])); // 14
console.log(sumSquares([1,4,9])); // 98
console.log(sumSquares([1,3,5,7])); // 84
console.log(sumSquares([1.4,4.2,0])); // 29
console.log(sumSquares([-2.4,1,1])); // 6
```






























































































































































































