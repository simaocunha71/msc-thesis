  if(array.length === 0) return array;

  let sortedArray = array.slice().sort((a, b) => a - b);

  if((array[0] + array[array.length - 1]) % 2 === 0) {
    sortedArray.reverse();
  }

  return sortedArray;
};

console.log(sortArray([])); // []
console.log(sortArray([5])); // [5]
console.log(sortArray([2, 4, 3, 0, 1, 5])); // [0, 1, 2, 3, 4, 5]
console.log(sortArray([2, 4, 3, 0, 1, 5, 6])); // [6, 5, 4, 3, 2, 1, 0]

```

## 6. Convert Binary to Decimal

```javascript
