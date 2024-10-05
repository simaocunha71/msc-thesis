/*
  We can get an array sorted in non-decreasing order by performing the following
  operation:
      You are allowed to perform right shift operation any number of times.
  
  One right shift operation means shifting all elements of the array by one
  position in the right direction. The last element of the array will be moved to
  the starting position in the array i.e. 0th index. 

  If it is possible to obtain the sorted array by performing the above operation
  then return true else return false.
  If the given array is empty then return true.

  Note: The given list is guaranteed to have unique elements.

  For Example:
  
  moveOneBall([3, 4, 5, 1, 2])==>true
  Explanation: By performin 2 right shift operations, non-decreasing order can
               be achieved for the given array.
  moveOneBall([3, 5, 4, 1, 2])==>false
  Explanation:It is not possible to get non-decreasing order for the given
              array by performing any number of right shift operations.
              
  */
const moveOneBall = (arr) => {

  // Write your code here
  if (arr.length === 0) return true;
  for (let i = arr.length - 2; i >= 0; i--) {
    if (arr[i] > arr[i + 1]) {
      let j = i + 1;
      while (arr[i] > arr[j]) j++;
      if (j === arr.length) return false;
      let temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    }
  }
  return true;
};
