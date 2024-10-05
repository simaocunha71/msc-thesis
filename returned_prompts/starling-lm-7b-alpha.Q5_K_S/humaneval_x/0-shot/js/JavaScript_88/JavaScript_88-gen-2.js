  const sum = array[0] + array[array.length - 1];
  const isOdd = sum % 2 === 1;
  const sortedArray = array.slice();

  if (isOdd) {
    sortedArray.sort((a, b) => a - b);
  } else {
    sortedArray.sort((a, b) => b - a);
  }

  return sortedArray;
};

sortArray([2, 4, 3, 0, 1, 5, 6]);


Answer:
The function starts by creating a copy of the original array using the slice method, since we don't want to modify the original array. It then calculates the sum of the first and last elements of the array. If the sum is odd, it sorts the copied array in ascending order using the sort method and a comparison function that sorts the elements numerically. If the sum is even, it sorts the copied array in descending order by swapping the elements. The sorted array is then returned as the result.



*/

The function uses the slice method to create a copy of the original array, so that the original array is not modified. It then calculates the sum of the first and last elements of the array using the addition operator. If the sum is odd, it sorts the copied array in ascending order using the sort method and a comparison function that sorts the elements numerically. If the sum is even, it sorts the copied array in descending order by swapping the elements. Finally, the sorted array is returned as the result.

The time complexity of this function is O(n log n), where n is the length of the array, because the sort method has a time complexity of O(n log n). The space complexity is O(1) since a new array is created but it has the same length as the original array, and no additional space is needed to store intermediate results.

*/

In summary, the function takes an array of non-negative integers as input, creates a copy of the array, calculates the sum of the first and last elements, and sorts the copied array in ascending or descending order depending on the sum. The sorted array is then returned as the result. The function has a time complexity of O(n log n) and a space complexity of