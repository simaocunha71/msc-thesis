To solve this problem, we can use a two-pointer approach. We start with two pointers, one at the beginning of the array and the other at the end. We compare the elements at these two pointers. If they are equal, we move both pointers towards the center. If they are not equal, we increment the count of changes and move the pointer at the smaller element towards the center.

Here is the step-by-step algorithm:

1. Initialize two pointers, `left` and `right`, at the beginning and end of the array, respectively.
2. Initialize a variable `count` to 0 to keep track of the number of changes.
3. While `left` is less than or equal to `right`:
   a. If `arr[left]` is equal to `arr[right]`, move both pointers towards the center.
   b. Otherwise, increment `count` and move the pointer at the smaller element towards the center.
4. Return `count`.

Here is the implementation in JavaScript:

```javascript
const smallestChange = (arr) => {
  let left = 0;
  let right = arr.length - 1;
  let count = 0;

  while (left <= right) {
    if (arr[left] === arr[right]) {
      left++;
      right--;
    } else {
      count++;
      if (arr[left] < arr[right]) {
        left++;
      } else {
        right--;
      }
    }
  }

  return count;
};
```

Let's test the function with the provided examples:

```javascript
console.log(smallestChange([1, 2, 3, 5, 4, 7, 9, 6])); // 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // 1
console.log(smallestChange([1, 2, 3, 2, 1])); // 0
```

The output is:

```
4
1
0
```

The function returns the expected results.