let seen = new Set();

  return numbers.filter(n => {
    if (seen.has(n)) {
      return false;
    } else {
      seen.add(n);
      return true;
    }
  });
}

console.log(removeDuplicates([1, 2, 3, 2, 4]));


This program works by creating a new Set object, which only stores unique values. It then uses the Array.filter() method to create a new array that includes only the elements that are not in the Set. In JavaScript, Set.has(value) returns true if the Set contains value, and false otherwise. When a value is added to the Set, it will not be added if it is already in the Set. This ensures that only unique values are included in the new array.


A: Here is a solution using the filter function in Javascript:

```javascript
let removeDuplicates = (numbers) => {
    return numbers.filter((value, index, self) => {
        return self.indexOf(value) === index;
    });
}

console.log(removeDuplicates([1, 2, 3, 2, 4]));  // Output: [1, 2, 3, 4]
```

This solution uses the filter function to create a new array that includes only the elements for which the callback function returns true. The callback function uses the indexOf method to check if the current value is the first occurrence of the value in the array. If it is, indexOf will return the index of the value, and the condition self.indexOf(value) === index will be true. This ensures that only the first occurrence of each value is included in the new array.

Please note that this solution does not preserve the original order of the elements in the array. If you want to preserve the original order, you will need to use a different approach, like the one provided by the other answer.

```javascript
let removeDuplicates = (numbers) => {
    let result = [];
    numbers.forEach((num) => {
        if (!result.includes(num)) {
            result.push(num);
        }
    });
    return result;
}

console.log(