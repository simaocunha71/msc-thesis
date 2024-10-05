/*Create a function which returns the largest index of an element which
  is not greater than or equal to the element immediately preceding it. If
  no such element exists then return -1. The given array will not contain
  duplicate values.

  Examples:
  canArrange([1,2,4,3,5]) = 3
  canArrange([1,2,3]) = -1
  */
const canArrange = (arr) => {
  let last = arr[0];
  let index = -1;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < last) {
      index = i;
      break;
    }
    last = arr[i];
  }
  return index;
}
console.log(canArrange([1,2,4,3,5])) // 3
console.log(canArrange([1,2,3])) // -1
console.log(canArrange([3,4,5,1,2])) // 3