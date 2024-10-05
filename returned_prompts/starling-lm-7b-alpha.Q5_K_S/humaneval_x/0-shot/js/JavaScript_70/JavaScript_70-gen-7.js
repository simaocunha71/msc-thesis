  let sortedList = lst.slice();
  while (sortedList.length > 0) {
    let minIndex = sortedList.indexOf(Math.min(...sortedList));
    sortedList.splice(minIndex, 1);
    let maxIndex = sortedList.indexOf(Math.max(...sortedList));
    sortedList.splice(maxIndex, 1);
  }
  return sortedList;
};

strangeSortList([5, 5, 5, 5]);

// Explanation
// The function starts by copying the original list to a new array called `sortedList`. This is done to prevent the original list from being modified during the sorting process.

// The `while` loop is used to repeatedly find the minimum and maximum values in the `sortedList` array, remove them, and then move on to the next pair of minimum and maximum values. This process continues until the `sortedList` array is empty.

// Inside the `while` loop, the `indexOf` function is used to find the index of the minimum value in the `sortedList` array. The `Math.min(...sortedList)` function is used to find the minimum value in the `sortedList` array. The minimum value is then removed from the `sortedList` array using the `splice` function.

// Similarly, the `indexOf` function is used to find the index of the maximum value in the `sortedList` array. The `Math.max(...sortedList)` function is used to find the maximum value in the `sortedList` array. The maximum value is then removed from the `sortedList` array using the `splice` function.

// The `sortedList` array is checked after each iteration of the `while` loop to ensure that it is empty. If the `sortedList` array is not empty, the loop continues to the next iteration. If the `sortedList` array is empty, the `while` loop ends and the function returns the sorted list.

// It's important to note that the `sortedList` array is modified in-place during each iteration of the `while` loop. This means that the changes made to the `sortedList` array are permanent and cannot be