  if(arr.length <= 1) return true;
  let count = 0;
  for(let i = 0; i < arr.length - 1; i++){
    if(arr[i] > arr[i+1]){
      count++;
    }
  }
  if(arr[arr.length-1] > arr[0]) count++;
  return count <= 1;
}

console.log(moveOneBall([3, 4, 5, 1, 2])) // true
console.log(moveOneBall([3, 5, 4, 1, 2])) // false
console.log(moveOneBall([2, 3, 4, 5, 1])) // true
console.log(moveOneBall([1, 1, 1, 1, 1])) // true
console.log(moveOneBall([])) // true

This solution works by counting the number of elements that are larger than the next one. If there is more than one such pair, it means we need more than one operation to sort the array. If there is exactly one such pair, it means we can sort the array with one operation.

For the edge case of the last element being larger than the first one, we increment the count by 1. If count is more than 1, return false; otherwise, return true.
*/

const moveOneBall = (arr) => {
  if(arr.length <= 1) return true;
  let count = 0;
  for(let i = 0; i < arr.length - 1; i++){
    if(arr[i] > arr[i+1]){
      count++;
    }
  }
  if(arr[arr.length-1] > arr[0]) count++;
  return count <= 1;
}

console.log(moveOneBall([3, 4, 5, 1, 2])) // true
console.log(moveOneBall([3, 5, 4, 1, 2])) // false
console.log(moveOneBall([2, 3, 4, 5, 1])) // true
console.log(