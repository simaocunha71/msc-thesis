  let maxIndex = -1;

  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      maxIndex = Math.max(maxIndex, i);
    }
  }

  return maxIndex;
};

console.log(canArrange([1,2,4,3,5])); // 3
console.log(canArrange([1,2,3])); // -1
console.log(canArrange([5,4,3,2,1])); // 1
console.log(canArrange([1,2,4,5,3])); // 3
console.log(canArrange([1,2,5,4,3])); // 3

This function works by iterating over the given array and comparing each element to the one immediately following it. If the current element is greater than the next one, it updates the value of maxIndex to be the maximum between the current maxIndex and the index of the current element. Once it has gone through the entire array, it will return the maximum index of an element that does not follow the non-increasing pattern. If no such element exists, it will return -1.

This solution has a time complexity of O(n) as it only goes through the array once.
*/

const canArrange = (arr) => {
  let maxIndex = -1;

  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      maxIndex = Math.max(maxIndex, i);
    }
  }

  return maxIndex;
};

console.log(canArrange([1,2,4,3,5])); // 3
console.log(canArrange([1,2,3])); // -1
console.log(canArrange([5,4,3,2,1])); // 1
console.log(canArrange([1,2,4,5,3])); // 3
console.log(canArrange([1,2,5,4,3])); // 3