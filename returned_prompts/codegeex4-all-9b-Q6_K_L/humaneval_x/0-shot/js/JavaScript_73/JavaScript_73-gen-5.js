To solve this problem, we need to find the minimum number of elements that need to be changed to make the array palindromic. A palindromic array is an array that reads the same backwards and forwards.

We can iterate through the array and compare each element with its corresponding element from the end of the array. If the elements are not equal, we need to change one of them to make them equal. We can count the number of such changes required to make the array palindromic.

Here is the implementation of the `smallestChange` function:

```javascript
const smallestChange = (arr) => {
  let changes = 0;
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    if (arr[left] !== arr[right]) {
      changes++;
    }
    left++;
    right--;
  }

  return changes;
};
```

Let's test the function with the provided examples:

```javascript
console.log(smallestChange([1, 2, 3, 5, 4, 7, 9, 6])); // 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // 1
console.log(smallestChange([1, 2, 3, 2, 1])); // 0
```

The output will be:

```
4
1
0
```

The time complexity of this solution is O(n), where n is the length of the array.