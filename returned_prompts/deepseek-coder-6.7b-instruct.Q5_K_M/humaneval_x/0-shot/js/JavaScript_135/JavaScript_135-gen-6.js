  for (let i = arr.length - 1; i > 0; i--) {
    if (arr[i] < arr[i - 1]) {
      return i;
    }
  }
  return -1;
}

console.log(canArrange([1,2,4,3,5])); // 3
console.log(canArrange([1,2,3])); // -1
console.log(canArrange([5, 4, 3, 2, 1])); // 0
console.log(canArrange([1, 3, 5, 2, 4])); // 3

*/

The function starts from the end of the array and checks each element if it is less than the preceding element. The index of the first occurrence of this condition is returned. If no such index is found, the function returns -1.

The time complexity of this function is O(n) because it only loops through the array once. The space complexity is O(1) as it only uses a few variables and does not use any data structures that grow with the input size.

*/

function canArrange(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
      if (arr[i] < arr[i - 1]) {
        return i;
      }
    }
    return -1;
  }

console.log(canArrange([1, 2, 4, 3, 5])); // 3
console.log(canArrange([1, 2, 3])); // -1
console.log(canArrange([5, 4, 3, 2, 1])); // 0
console.log(canArrange([1, 3, 5, 2, 4])); // 3















































































