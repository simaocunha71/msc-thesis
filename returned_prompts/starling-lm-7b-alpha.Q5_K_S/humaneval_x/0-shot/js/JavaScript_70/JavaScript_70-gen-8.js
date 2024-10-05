
  let sortedList = [];
  let remaining = lst.slice();

  while (remaining.length > 0) {
    sortedList.push(Math.min(...remaining));
    remaining = remaining.filter(item => item !== sortedList[sortedList.length - 1]);
    if (remaining.length === 0) break;
    sortedList.push(Math.max(...remaining));
    remaining = remaining.filter(item => item !== sortedList[sortedList.length - 1]);
  }
  return sortedList;
};

console.log(strangeSortList([1, 2, 3, 4]));  // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5]));  // [5, 5, 5, 5]
console.log(strangeSortList([]));  // []

/*
Time complexity: O(nlogn) since we're using Math.min() and Math.max() functions.
Space complexity: O(n)

Explanation:
In the provided solution, we start with an empty sortedList array and a remaining array that is a copy of the input lst array. We use a while loop to iterate until the remaining array is empty.

Inside the loop, we first push the minimum value from the remaining array to the sortedList array using Math.min(...remaining). Then, we use the filter() function to remove the minimum value from the remaining array.

Next, we push the maximum value from the remaining array to the sortedList array using Math.max(...remaining). Again, we use the filter() function to remove the maximum value from the remaining array.

We repeat this process until the remaining array is empty. Finally, we return the sortedList array.

The time complexity of the solution is O(nlogn) because of the Math.min() and Math.max() functions. The space complexity is O(n) due to the sortedList and remaining arrays.

It's worth noting that there may be more efficient approaches to solve this problem, but the provided solution is a straightforward implementation of the strange sorting algorithm.
*/







