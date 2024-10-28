  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 3 === 0 && i % 4 !== 0) {
      sum += lst[i] * lst[i]
    } else if (i % 4 === 0) {
      sum += lst[i] * lst[i] * lst[i]
    } else {
      sum += lst[i]
    }
  }
  return sum;
};

console.log(sumSquares([1, 2, 3])); // 6
console.log(sumSquares([])); // 0
console.log(sumSquares([-1, -5, 2, -1, -5])); // -126

*/

// In this function, the for loop goes through each element in the list. 
// If the index of the element is a multiple of 3 and not a multiple of 4, the function squares the element and adds it to the sum. 
// If the index of the element is a multiple of 4, the function cubes the element and adds it to the sum. 
// If the index of the element is neither a multiple of 3 nor a multiple of 4, the function simply adds the element to the sum. 
// Finally, the function returns the sum.

// The time complexity of this function is O(n) where n is the length of the list because it goes through each element in the list once. 
// The space complexity is O(1) because it uses a constant amount of space to store the sum and the elements of the list.

*/

// The function sumSquares takes a list of integers as input.
// It initializes a variable sum to 0.
// Then it goes through each element in the list.
// If the index of the element is a multiple of 3 and not a multiple of 4, it squares the element and adds it to sum.
// If the index of the element is a multiple of 4, it cubes the element and adds it to sum.
// If the index of the element is neither a multiple of 3 nor a multiple of 4, it adds the