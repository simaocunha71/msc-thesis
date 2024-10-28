Here is a solution in JavaScript:
```
const smallestChange = (arr) => {
  let count = 0;
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    if (arr[left] !== arr[right]) {
      count++;
    }
    left++;
    right--;
  }

  return count;
};
```
This function uses a two-pointer approach to find the minimum number of changes needed to make the array palindromic. The `left` and `right` pointers start at the beginning and end of the array, respectively. The function iterates through the array, comparing the elements at the `left` and `right` indices. If the elements are not equal, it increments the `count` variable. The function continues until the `left` and `right` pointers meet in the middle of the array. The `count` variable represents the minimum number of changes needed to make the array palindromic.

You can test this function with the examples you provided:
```
console.log(smallestChange([1,2,3,5,4,7,9,6])); // Output: 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // Output: 1
console.log(smallestChange([1, 2, 3, 2, 1])); // Output: 0
```
I hope this helps! Let me know if you have any questions. 😊

---

**Explanation:**

1. We initialize a variable `count` to keep track of the minimum number of changes needed to make the array palindromic.
2. We initialize two pointers, `left` and `right`, to the beginning and end of the array, respectively.
3. We enter a while loop that continues until the `left` and `right` pointers meet in the middle of the array.
4. Inside the loop, we compare the elements at the `left` and `right` indices. If they are not equal, we increment the `count` variable.
5. We increment the `left` pointer and decrement the `right` pointer to move towards the middle of the array.
6. Once the loop exits, the `count` variable represents the minimum number of changes needed to make the array palindromic.
7. We return the `count` variable as the result.

**Time complexity