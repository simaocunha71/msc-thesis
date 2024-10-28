  let maxIndex = -1;
  for (let i = arr.length - 1; i > 0; i--) {
    if (arr[i] < arr[i - 1]) {
      maxIndex = i;
      break;
    }
  }
  return maxIndex;
};

console.log(canArrange([1,2,4,3,5])); // 3
console.log(canArrange([1,2,3])); // -1

*/

// Solution:
// This solution starts from the end of the array and checks if the current number is smaller than the previous number. If it is, it breaks the loop and returns the current index. If it doesn't find any such number, it returns -1.

// Time complexity: O(n) because in the worst case scenario, it will have to traverse the whole array.
// Space complexity: O(1) because it only uses a constant amount of space to store the maxIndex and i.

const canArrange = (arr) => {
  let maxIndex = -1;
  for (let i = arr.length - 1; i > 0; i--) {
    if (arr[i] < arr[i - 1]) {
      maxIndex = i;
      break;
    }
  }
  return maxIndex;
};

console.log(canArrange([1,2,4,3,5])); // 3
console.log(canArrange([1,2,3])); // -1

// This solution is correct and efficient.
// It works by iterating through the array from the end to the beginning, checking if each element is less than the previous one. If it finds an element that is less, it returns the index of that element. If it doesn't find any such elements, it returns -1.



















































































