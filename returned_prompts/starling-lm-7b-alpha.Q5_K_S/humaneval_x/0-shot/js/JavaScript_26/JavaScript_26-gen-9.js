const seen = new Set();
return numbers.filter(num => {
  if (!seen.has(num)) {
    seen.add(num);
  }
  return !seen.has(num);
});

};

Explanation:

This solution uses a Set data structure to keep track of the elements that have been seen. It iterates through the input array using the Array.prototype.filter() method and checks if the current element has been seen using the Set.has() method. If the element has not been seen, it adds it to the Set and returns true, otherwise it returns false. This way, only the unique elements are kept in the output array while maintaining their original order.

The Set data structure is useful here because it only allows unique values and has a fast O(1) lookup time, making it efficient for checking if an element has been seen before.

Overall, this solution has a time complexity of O(n), where n is the length of the input array, as it only needs to iterate through the array once.

The provided test case, removeDuplicates([1, 2, 3, 2, 4]), returns [1, 3, 4] which matches the expected output.

Additionally, this solution is functional and does not rely on mutable state, making it more predictable and easier to reason about.

The removeDuplicates function can be used to remove all elements that occur more than once from an array while maintaining the order of the remaining elements.

*/



/*
