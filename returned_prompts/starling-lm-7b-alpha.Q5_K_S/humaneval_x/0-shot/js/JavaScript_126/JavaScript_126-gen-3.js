To solve this problem, we can compare each number in the list to the next number in the list. If the current number is greater than the next number, we can return false because the list is not sorted in ascending order. If we go through the entire list and don't find any out of order numbers, we can return true.

Here's a step-by-step breakdown of the solution:

1. Define the function isSorted that takes a single parameter, lst, which is the list of numbers.
2. Initialize a variable, index, to keep track of the current position in the list. Set it to 0 initially.
3. Initialize a variable, nextIndex, to keep track of the next position in the list. Set it to 1 initially.
4. Enter a while loop that continues as long as index is less than the length of the list minus 1. This loop will compare each number in the list to the next number.
5. Inside the loop, compare the number at index to the number at nextIndex. If the number at index is greater than the number at nextIndex, return false because the list is not sorted in ascending order.
6. If the current number is not greater than the next number, increment index by 1 and set nextIndex to index + 1.
7. After the loop finishes, return true because all numbers in the list are in ascending order and there are no duplicate numbers.
8. Call the isSorted function with a sample list, such as [5], and log the result to the console using console.log.

Here's an example implementation of the solution in JavaScript:

```javascript
const isSorted = (lst) => {
  let index = 0;
  let nextIndex = 1;

  while (index < lst.length - 1) {
    if (lst[index] > lst[nextIndex]) {
      return false;
    }
    index++;
    nextIndex = index + 1;
  }

  return true;
}

console.log(isSorted([5])); // true
```

In this example, the isSorted function takes a single parameter, lst, which is the list of numbers. It initializes two variables, index and nextIndex, to keep track