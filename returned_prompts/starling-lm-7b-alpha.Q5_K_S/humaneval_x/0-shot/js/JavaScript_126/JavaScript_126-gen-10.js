To solve this problem, you can follow these steps:

1. First, you need to check if the length of the list is less than or equal to 1. If it is, then the list is considered sorted and you can return true. This is because a list with 0 or 1 element is trivially sorted.

2. Next, you need to compare the first and second elements of the list. If they are not in ascending order, then the list is not sorted and you can return false. This can be done using an if statement.

3. Then, you can use a for loop to iterate through the remaining elements of the list. For each element, compare it with the next element. If they are not in ascending order, then the list is not sorted and you can return false. This can be done using an if statement inside the for loop.

4. After iterating through all the elements, if the for loop has finished without returning false, then the list is considered sorted and you can return true. This is because all the elements are in ascending order and there are no duplicates.

Here's an example implementation of the solution in JavaScript:

```javascript
const isSorted = (lst) => {
  if (lst.length <= 1) {
    return true;
  }
  
  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] > lst[i + 1]) {
      return false;
    }
  }
  
  return true;
};
```

This implementation first checks if the length of the list is less than or equal to 1. If it is, the function immediately returns true. Otherwise, it enters a for loop that compares each element with the next element. If any pair of adjacent elements is not in ascending order, the function returns false. If the loop completes without returning false, the function returns true, indicating that the list is sorted in ascending order with no duplicates.

You can use this function to check if a given list of numbers is sorted in ascending order without any duplicate elements.

Note: The function assumes that the input list contains only integers and does not include any negative numbers.

Here are some test cases to validate the function