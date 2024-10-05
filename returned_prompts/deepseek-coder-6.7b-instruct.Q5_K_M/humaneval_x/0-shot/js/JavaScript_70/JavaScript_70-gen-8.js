  // Sort the list in ascending order
  lst.sort((a, b) => a - b);

  // Initialize an empty result list
  let res = [];

  // While the list is not empty
  while (lst.length) {
    // Push the minimum value to the result
    res.push(lst.shift());

    // If the list is not empty
    if (lst.length) {
      // Push the maximum value to the result
      res.push(lst.pop());
    }
  }

  // Return the result list
  return res;
}
console.log(strangeSortList([1, 2, 3, 4])) // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5])) // [5, 5, 5, 5]
console.log(strangeSortList([])) // []


Explanation:
The function sorts the list in ascending order. It then iteratively takes the smallest and largest remaining numbers from the list and adds them to the result. This continues until all numbers have been added to the result.
*/

// Solution 2
/*
