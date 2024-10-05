To solve this problem, you can follow these steps:

1. Check if the length of the list is less than or equal to 1. If so, return true as a single element list is considered sorted.
2. Create a variable 'prev' and assign the first element of the list to it.
3. Iterate through the rest of the elements in the list using the 'forEach' method.
4. Inside the iteration, check if the current element is greater than the previous element. If so, return false as it indicates that the list is not sorted in ascending order.
5. After the iteration, assign the current element to the 'prev' variable. This step is necessary to update the 'prev' variable for the next iteration.
6. After the iteration, return true as all the elements in the list are in ascending order.

Here's the code that implements the above steps:

```javascript
const isSorted = (lst) => {
  if (lst.length <= 1) {
    return true;
  }

  let prev = lst[0];
  lst.forEach((element, index) => {
    if (index === 0) {
      prev = element;
    } else if (element > prev) {
      return false;
    } else {
      prev = element;
    }
  });

  return true;
};
```

You can use the 'isSorted' function to check if a list of numbers is sorted in ascending order. It will return true if the list is sorted and false otherwise.

*/

/* Given a list of numbers, return whether or not they are sorted
  in ascending order. If list has more than 1 duplicate of the same
  number, return false. Assume no negative numbers and only integers.
  Examples
  isSorted([5]) ➞ true
  isSorted([1, 2, 3, 4, 5]) ➞ true
  isSorted([1, 3, 2, 4, 5]) ➞ false
  isSorted([1, 2, 3, 4, 5, 6]) ➞ true
  isSorted([1, 2, 3