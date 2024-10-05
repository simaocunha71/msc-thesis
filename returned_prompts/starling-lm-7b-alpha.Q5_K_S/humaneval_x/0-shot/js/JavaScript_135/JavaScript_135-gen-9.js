let max = -1;
let i = 0;
while (i < arr.length) {
  let j = i + 1;
  while (j < arr.length) {
    if (arr[j] > arr[i]) {
      max = i;
      break;
    }
    j++;
  }
  i++;
}
return max;

};

/*
Explanation:
The function iterates through the array, finding the next smallest element
in the array. If the next smallest element is smaller than the element at
the current index, then the current index is the maximum index of an element
that is not greater than or equal to the element immediately preceding it. If
no such element exists, then -1 is returned.

However, this solution has a time complexity of O(n^2), which can be improved
to O(n) by using a different approach.
*/

// Alternative solution with time complexity O(n)
const canArrange = (arr) => {
  let max = -1;
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] < arr[i + 1]) {
      max = i;
      break;
    }
  }
  return max;
};

*/

/*
Explanation:
The alternative solution iterates through the array, comparing each element
to the next element. If an element is found to be smaller than the next element,
then the index of that element is the maximum index of an element that is not
greater than or equal to the element immediately preceding it. If no such element
exists, then -1 is returned.

This solution has a time complexity of O(n), which is much more efficient than
the previous solution with a time complexity of O(n^2).
*/

// Test cases
console.log(canArrange([1, 2, 4, 3, 5])); // 3
console.log(canArrange([1, 2, 3])); // -1
console.log(canArrange([1, 2, 3, 4, 5])); // -1
console.log(canArrange([