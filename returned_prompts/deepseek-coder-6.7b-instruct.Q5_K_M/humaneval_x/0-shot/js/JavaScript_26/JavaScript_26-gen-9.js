  const count = {};
  const result = [];

  for (let number of numbers) {
    count[number] = (count[number] || 0) + 1;
  }

  for (let number of numbers) {
    if (count[number] === 1) {
      result.push(number);
    }
  }

  return result;
};

console.log(removeDuplicates([1, 2, 3, 2, 4]));
// Output: [1, 3, 4]

Explanation:
  First, we create a count object to keep track of how many times each number appears in the array. 

  Then, we go through the array again, and if the count for a number is 1, we add it to the result array.

  Finally, we return the result array, which contains the numbers that only appear once in the original array, in the same order as they appeared in the original array.

  This solution has a time complexity of O(n), where n is the size of the input array. It also has a space complexity of O(n), since in the worst case (when all elements are unique), we need to store all elements in the count and result arrays.
*/

/*
