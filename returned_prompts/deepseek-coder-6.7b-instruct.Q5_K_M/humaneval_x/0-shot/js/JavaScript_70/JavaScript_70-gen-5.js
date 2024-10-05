  //Sort the given list in ascending order
  lst.sort((a, b) => a - b);

  //Create an empty array to store the result
  let result = [];

  //Loop while there are elements in the list
  while (lst.length) {
    //Remove the first element and push it to the result
    result.push(lst.shift());

    //If there are still elements in the list,
    //remove the last element and push it to the result
    if (lst.length) {
      result.push(lst.pop());
    }
  }

  //Return the result
  return result;
};

console.log(strangeSortList([1, 2, 3, 4])); //[1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5])); //[5, 5, 5, 5]
console.log(strangeSortList([])); // []
```

This solution works by first sorting the given list in ascending order. Then it creates an empty array to store the result. It enters a loop, removing the first and last elements from the list and appending them to the result. This continues until there are no more elements in the list. Finally, it returns the result.

This solution has a time complexity of O(n log n) due to the sorting operation, and a space complexity of O(n) for storing the result.

Please note that the sorting operation will modify the original list, if you want to keep the original list unchanged, you need to make a copy of it before sorting.

Also, this solution assumes that the given list only contains integers. If the list can contain other types of values, you may need to add additional error checking code to handle these cases.
  */
```

















































































