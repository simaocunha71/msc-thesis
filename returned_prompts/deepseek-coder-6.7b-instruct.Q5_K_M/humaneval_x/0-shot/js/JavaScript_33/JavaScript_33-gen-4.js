  const sortedArray = l.slice().sort((a, b) => a - b);
  const resultArray = [];

  for (let i = 0; i < l.length; i++) {
    if ((i + 1) % 3 === 0) {
      resultArray.push(sortedArray.shift());
    } else {
      resultArray.push(l[i]);
    }
  }

  return resultArray;
};

console.log(sortThird([5, 6, 3, 4, 8, 9, 2]));

*/

const sortThird = (l) => {
  const sortedArray = l.slice().sort((a, b) => a - b);
  const resultArray = [];

  for (let i = 0; i < l.length; i++) {
    if ((i + 1) % 3 === 0) {
      resultArray.push(sortedArray.shift());
    } else {
      resultArray.push(l[i]);
    }
  }

  return resultArray;
};

console.log(sortThird([5, 6, 3, 4, 8, 9, 2])); // [2, 6, 3, 4, 8, 9, 5]

```

## 3. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

```javascript
const containsDuplicate = (nums) => {
  const numSet = new Set();

  for (let num of nums) {
    if (numSet.has(num)) {
      return true;
    }
    numSet.add(num);
  }

  return false;
};

console.log(containsDuplicate([1, 2, 3, 4])); // false
console.log(containsDuplicate([1, 2, 3, 1])); // true
```

## 4. Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input