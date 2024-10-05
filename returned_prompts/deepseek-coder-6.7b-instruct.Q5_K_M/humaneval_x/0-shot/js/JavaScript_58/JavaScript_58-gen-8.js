  let commonNums = l1.filter(n => l2.includes(n));
  let uniqueNums = [...new Set(commonNums)];
  return uniqueNums.sort((a, b) => a - b);
}

console.log(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]));
console.log(common([5, 3, 2, 8], [3, 2]));

*/


// Test cases
console.log(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])); // Should return [1, 5, 653]
console.log(common([5, 3, 2, 8], [3, 2])); // Should return [2, 3]
console.log(common([], [])); // Should return []
console.log(common([1], [1])); // Should return [1]
console.log(common([1, 2, 3], [1, 2, 3])); // Should return [1, 2, 3]
console.log(common([1, 2, 3], [4, 5, 6])); // Should return []
console.log(common([1, 2, 2, 3], [2, 2, 3])); // Should return [2, 3]
console.log(common([1, 2, 2, 3], [2, 2, 2, 3])); // Should return [2, 3]
console.log(common([1, 2, 2, 3], [1, 1, 2, 2])); // Should return [1, 2]
console.log(common([1, 1, 2, 2], [1, 2, 2, 3])); // Should return [1, 2]

```
