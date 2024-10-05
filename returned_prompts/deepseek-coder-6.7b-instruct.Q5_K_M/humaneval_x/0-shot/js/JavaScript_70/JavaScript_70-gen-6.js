  const sorted = [...lst].sort((a, b) => a - b);
  const result = [];
  
  while (sorted.length) {
    result.push(sorted.shift());
    if (sorted.length) {
      result.push(sorted.pop());
    }
  }
  
  return result;
};

console.log(strangeSortList([1, 2, 3, 4])); // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5])); // [5, 5, 5, 5]
console.log(strangeSortList([])); // []

/*
  Explanation:
  We sort the array first and then we start to take elements from the start and end of the array alternatively.
  We push elements into result array one by one and finally return the result array.
 */

/*
  Test case:
  console.log(strangeSortList([1, 2, 3, 4])); // [1, 4, 2, 3]
  console.log(strangeSortList([5, 5, 5, 5])); // [5, 5, 5, 5]
  console.log(strangeSortList([])); // []
 */


/*
  Solution Complexity:
  The complexity of the solution is O(n log n) because of the sorting, where n is the length of the input array.
 */
```

---
## **[⬆ Back to Top](#table-of-contents)**


























































































































