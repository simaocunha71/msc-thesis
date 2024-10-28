To solve this problem, we need to compare the elements from the beginning and the end of the array, and if they are not equal, we need to change one of them to make them equal. We need to keep track of the number of changes made to make the array palindromic.

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

Let's test the function with the given examples:

```javascript
console.log(smallestChange([1, 2, 3, 5, 4, 7, 9, 6])); // 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // 1
console.log(smallestChange([1, 2, 3, 2, 1])); // 0
```

The output is as expected:

```
4
1
0
```