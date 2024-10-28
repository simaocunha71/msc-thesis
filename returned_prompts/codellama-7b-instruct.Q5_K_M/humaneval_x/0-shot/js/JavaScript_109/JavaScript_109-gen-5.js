/*

  There are two ways to solve this problem:
  a) Check if the array is already sorted in ascending order
  b) Check if the array is already sorted in descending order

  If a) or b) is true, return true.

  If not, check if the array is sorted in descending order. 
  If it is, return false.

  If not, check if the array is sorted in ascending order. 
  If it is, return true.

  If not, then return false.

  */
const moveOneBall = (arr) => {

  // a) check if the array is sorted in ascending order
  if (arr.every((val, index) => index === 0 || val >= arr[index - 1])) {
    return true
  }

  // b) check if the array is sorted in descending order
  if (arr.every((val, index) => index === arr.length - 1 || val <= arr[index + 1])) {
    return false
  }

  // c) check if the array is sorted in descending order
  if (arr.every((val, index) => index === arr.length - 1 || val >= arr[index + 1])) {
    return false
  }

  // d) check if the array is sorted in ascending order
  if (arr.every((val, index) => index === 0 || val <= arr[index - 1])) {
    return true
  }

  // e) return false
  return false
}

/*

  Time Complexity: O(N)
  Space Complexity: O(1)

  */

