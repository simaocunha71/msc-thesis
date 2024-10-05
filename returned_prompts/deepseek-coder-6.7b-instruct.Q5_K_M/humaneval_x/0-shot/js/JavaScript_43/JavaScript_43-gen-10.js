  const map = {};
  for (let i = 0; i < l.length; i++) {
    if (map[-l[i]]) {
      return true;
    }
    map[l[i]] = true;
  }
  return false;
};

console.log(pairsSumToZero([2, 4, -5, 3, 5, 7]));
console.log(pairsSumToZero([1, 3, 5, 0]));
console.log(pairsSumToZero([1, 3, -2, 1]));
console.log(pairsSumToZero([1, 2, 3, 7]));
console.log(pairsSumToZero([1]));
```

This program creates a map of numbers to true, then for every number in the list, it checks if the negation of the number is in the map. If it is, it returns true because there are two distinct elements that sum to zero. If it finishes going through the list and doesn't find two numbers that sum to zero, it returns false.

The time complexity of this solution is O(n), where n is the length of the list, because it goes through the list once. The space complexity is also O(n), because in the worst case (where all the numbers in the list are distinct) it stores a number from the list in the map for each one.

The function `pairsSumToZero` takes in an array of numbers and returns a boolean indicating whether there are two distinct numbers in the array that sum to zero. If such a pair exists, it returns true; otherwise, it returns false.
*/

// Do not edit this line;
module.exports = pairsSumToZero;
```

## Complexity Analysis

The time complexity of the `pairsSumToZero` function is O(n) where n is the length of the input list `l`. This is because the function uses a single loop to iterate over the elements of the list.

The space complexity of the `pairsSumToZero` function is also O(n) in the worst-case scenario. This is because in the worst case, all the elements of the list are distinct, and hence, all the elements of the list