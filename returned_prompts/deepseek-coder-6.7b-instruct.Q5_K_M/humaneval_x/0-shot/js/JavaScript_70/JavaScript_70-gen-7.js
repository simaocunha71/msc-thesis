  lst.sort((a, b) => a - b)
  let result = []
  while (lst.length) {
    result.push(lst.shift())
    if (lst.length) {
      result.push(lst.pop())
    }
  }
  return result
}

console.log(strangeSortList([1, 2, 3, 4]))  // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5]))  // [5, 5, 5, 5]
console.log(strangeSortList([]))  // []

// The function works by sorting the original list in ascending order.
// Then it takes the smallest and largest values from the sorted list
// and adds them to a new list in alternating order until the original list is empty.
// The new list is then returned.
// This results in the smallest and largest values being alternated in the new list,
// which is the desired "strange" order.

// The time complexity of this function is O(n log n) due to the sorting operation,
// where n is the length of the input list.
// The space complexity is O(n), as a new list is created to hold the result.

// This function can be further optimized, for example by using a two-pointer approach
// to avoid the use of the shift and pop methods, which could potentially reduce the time complexity.
```



## 2. 

```javascript
