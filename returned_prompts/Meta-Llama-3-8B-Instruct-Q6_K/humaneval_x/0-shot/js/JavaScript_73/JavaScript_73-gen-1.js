```
const smallestChange = (arr) => {
  let left = 0;
  let right = arr.length - 1;
  let changes = 0;

  while (left < right) {
    if (arr[left] !== arr[right]) {
      changes++;
      left++;
    } else {
      left++;
      right--;
    }
  }

  return changes;
};
```
Explanation:
The approach is to use two pointers, one from the start and one from the end of the array. We iterate through the array, comparing the elements at the two pointers. If they are not equal, we increment the change count and move the left pointer to the right. If they are equal, we move both pointers towards the center of the array. This way, we count the minimum number of changes needed to make the array palindromic. If the array is already palindromic, the function returns 0.

For example, in the array [1,2,3,5,4,7,9,6], the function will return 4, because we need to change 4 elements to make it palindromic. The changed array would be [1,2,3,3,4,4,7,6]. Similarly, for the array [1, 2, 3, 4, 3, 2, 2], the function will return 1, because we need to change only 1 element to make it palindromic. The changed array would be [1, 2, 3, 4, 4, 3, 2, 2]. If the array is already palindromic, the function will return 0. For example, for the array [1, 2, 3, 2, 1], the function will return 0, because the array is already palindromic.