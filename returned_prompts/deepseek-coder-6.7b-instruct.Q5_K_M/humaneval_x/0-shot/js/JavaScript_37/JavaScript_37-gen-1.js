  let newArray = [];
  let evenArray = [];
  let oddArray = [];
  
  for (let i = 0; i < l.length; i++) {
    if (i % 2 === 0) {
      evenArray.push(l[i]);
    } else {
      oddArray.push(l[i]);
    }
  }
  
  evenArray.sort((a, b) => a - b);

  for (let i = 0; i < l.length; i++) {
    if (i % 2 === 0) {
      newArray.push(evenArray.shift());
    } else {
      newArray.push(oddArray[i - 1]);
    }
  }
  
  return newArray;
};

console.log(sortEven([1, 2, 3])); // [1, 2, 3]
console.log(sortEven([5, 6, 3, 4])); // [3, 6, 5, 4]
```

## Problem 3:

