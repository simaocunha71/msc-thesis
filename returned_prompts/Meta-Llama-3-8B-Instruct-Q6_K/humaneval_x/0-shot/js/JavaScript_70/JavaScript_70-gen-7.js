```
const strangeSortList = (lst) => {
  if (lst.length === 0) return [];
  const sortedList = lst.slice().sort((a, b) => a - b);
  const result = [];
  while (sortedList.length > 0) {
    result.push(sortedList.shift());
    if (sortedList.length > 0) {
      result.push(sortedList.pop());
    }
  }
  return result;
};
```  Strange sorting is achieved by sorting the list first, then iterating over it and pushing the smallest element to the result list, then the largest element, then the smallest again, and so on. This approach ensures that the smallest and largest elements are alternated in the result list. The `shift()` and `pop()` methods are used to remove and add elements to the front and end of the list, respectively. The `slice()` method is used to create a copy of the original list to avoid modifying it in place. The `while` loop continues until the original list is empty, at which point the result list is returned.  This solution works for both positive and negative integers, and it also handles the case where the input list is empty, returning an empty list in that case.  The time complexity of this solution is O(n log n) due to the sorting operation, where n is the length of the input list. The space complexity is O(n) for the result list and the temporary sorted list.  Here are some examples of the `strangeSortList` function in action:  ```
console.log(strangeSortList([1, 2, 3, 4])); // Output: [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5])); // Output: [5, 5, 5, 5]
console.log(strangeSortList([])); // Output: []
```  I hope this helps! Let me know if you have any questions.  ```javascript
```  Strange sorting is achieved by sorting the list first, then iterating over it and pushing the smallest element to the result list, then the largest element, then the smallest again, and so on. This approach ensures that the smallest and largest elements are alternated in the result list. The `shift()` and `pop()` methods are used to remove and add elements to the front and end of the list, respectively. The `slice()` method is used to create a copy of the