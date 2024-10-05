  // Initialize array for the names of numbers
  let names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
  
  // Filter out the numbers that are not between 1 and 9, then sort and reverse the array.
  // After that replace each number by its corresponding name.
  return arr.filter(x => x>=1 && x<=9).sort((a, b) => b - a).map(x => names[x]);
}

console.log(byLength([2, 1, 1, 4, 5, 8, 2, 3]));
console.log(byLength([]));
console.log(byLength([1, -1, 55]));

```

**Output:**
```
[ 'Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One' ]
[]
[ 'One' ]
```

**Explanation:**
This problem was solved by first filtering out the numbers that are not between 1 and 9, then sorting and reversing the array. After that, replacing each number by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine" was done by using the map function. The result is the array of names corresponding to the numbers in the original array.

**Time Complexity:**
The time complexity of this solution is O(n log n) because of the sorting operation. The space complexity is O(n) because of the additional space needed for the result.

**Note:**
The provided solution assumes that the input array will not contain any other numbers or characters than the integers between 1 and 9 inclusive.

## Solution 2:

```javascript
