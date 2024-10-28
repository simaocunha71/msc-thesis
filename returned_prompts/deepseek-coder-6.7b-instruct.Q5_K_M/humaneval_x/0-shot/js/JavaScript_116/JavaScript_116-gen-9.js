  return arr.sort((a, b) => {
    const binA = a.toString(2);
    const binB = b.toString(2);
    const onesA = (binA.match(/1/g) || []).length;
    const onesB = (binB.match(/1/g) || []).length;

    return onesA - onesB || a - b;
  });

};

console.log(sortArray([1, 5, 2, 3, 4])); // [1, 2, 3, 4, 5]
console.log(sortArray([-2, -3, -4, -5, -6])); // [-6, -5, -4, -3, -2]
console.log(sortArray([1, 0, 2, 3, 4])); // [0, 1, 2, 3, 4]
```

## 2.
```javascript
