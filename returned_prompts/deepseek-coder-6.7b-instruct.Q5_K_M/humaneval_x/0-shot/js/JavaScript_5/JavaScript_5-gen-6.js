  const interspersedArray = [];
  for (let i = 0; i < numbers.length; i++) {
    interspersedArray.push(numbers[i]);
    if (i !== numbers.length - 1) {
      interspersedArray.push(delimeter);
    }
  }
  return interspersedArray;
}

console.log(intersperse([], 4)); // []
console.log(intersperse([1, 2, 3], 4)); // [1, 4, 2, 4, 3]

// Time complexity: O(n), where n is the length of the input list
// Space complexity: O(n), where n is the length of the input list
```

## 4. Solution 2: Using JavaScript's spread syntax and map method

```javascript
