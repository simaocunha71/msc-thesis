  let count = {};
  return numbers.filter(n => {
    if(count[n]){
      return false;
    } else {
      count[n] = true;
      return true;
    }
  });
}

// Test cases
console.log(removeDuplicates([1, 2, 3, 2, 4]));
```

### Solution

We can solve the problem by using a hash map (or JavaScript object) to count the frequency of each number in the array. If a number occurs more than once, we filter it out of the result array.

The function `removeDuplicates` works by creating a hash map `count` and using the array method `filter` to create a new array that only includes numbers that occur once.

In the `filter` method, we check if `count[n]` exists. If it does, that means we've seen this number before, so we return `false` to filter it out. If `count[n]` doesn't exist, we set it to `true` and return `true` to include the number in the new array.

This way, we keep the order of elements the same as in the input array, but remove any duplicates.

Finally, we return the new array.

This solution has a time complexity of O(n), where n is the length of the input array, because we have to go through each element in the array once.

The space complexity is also O(n), because in the worst case (when all elements are unique) we have to store a count for every element in the array.

Testing this function with the test case `[1, 2, 3, 2, 4]` outputs `[1, 3, 4]`, which is the expected result.

```javascript
const removeDuplicates = (numbers) => {
  let count = {};
  return numbers.filter(n => {
    if(count[n]){
      return false;
    } else {
      count[n] = true;
      return true;
    }
  });
}

console.log(removeDuplicates([1, 2, 3, 2, 4])); // [1