  // Check if array is empty
  if (lst.length === 0) return null;

  // Initialize the smallest and second smallest elements as infinity
  let smallest = Infinity;
  let secondSmallest = Infinity;

  // Loop through the array
  for (let i = 0; i < lst.length; i++) {
    // If current element is smaller than smallest, update smallest and second smallest
    if (lst[i] < smallest) {
      secondSmallest = smallest;
      smallest = lst[i];
    } else if (lst[i] < secondSmallest && lst[i] > smallest) {
      // If current element is in between smallest and second smallest, update second smallest
      secondSmallest = lst[i];
    }
  }

  // If there's a second smallest element, return it
  return secondSmallest === Infinity ? null : secondSmallest;
}

console.log(nextSmallest([1, 2, 3, 4, 5])) // 2
console.log(nextSmallest([5, 1, 4, 3, 2])) // 2
console.log(nextSmallest([])) // null
console.log(nextSmallest([1, 1])) // null
```
This function works by initializing two variables, smallest and second smallest, to infinity. Then it loops through the array and updates smallest and second smallest whenever it finds a smaller or second smaller number. Finally, it returns secondSmallest if it exists (i.e. it's not infinity), otherwise it returns null.

It has a time complexity of O(n) because it loops through the array once.

It has a space complexity of O(1) because it only uses a constant amount of space to store smallest and second smallest.
</p>
</details>

---

#### 4. Longest Common Prefix

<details>
<summary>Click to expand</summary>
<p>

