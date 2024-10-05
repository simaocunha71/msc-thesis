Here is a JavaScript solution using a two-pointer approach:

```javascript
const smallestChange = (arr) => {
    let left = 0;
    let right = arr.length - 1;
    let changes = 0;

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

This function initializes two pointers, `left` and `right`, at the beginning and end of the array, respectively. It then enters a loop that continues until `left` is no longer less than `right`. Inside the loop, it checks if the elements at the current `left` and `right` indices are equal. If they are not, it increments the `changes` counter. It then increments `left` and decrements `right` to move the pointers closer to each other. At the end of the function, it returns the total number of changes needed to make the array palindromic.

For example, if we call `smallestChange([1,2,3,5,4,7,9,6])`, the function will return `4`, because we need to change the elements at indices `2`, `3`, `5`, and `6` to make the array palindromic. If we call `smallestChange([1, 2, 3, 4, 3, 2, 2])`, the function will return `1`, because we need to change the element at index `1` to make the array palindromic. If we call `smallestChange([1, 2, 3, 2, 1])`, the function will return `0`, because the array is already palindromic.