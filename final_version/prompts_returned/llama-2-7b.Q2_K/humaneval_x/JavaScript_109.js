/*We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
  numbers in the array will be randomly ordered. Your task is to determine if
  it is possible to get an array sorted in non-decreasing order by performing 
  the following operation on the given array:
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
  if(arr[0] === undefined){
    return true; // If this array has no elements then it is sufficient to perform only one left shift operation.
  }
  
  let tempArray = [...arr]; // Create a temporary copy of the given list so that we can remove or change its contents freely.
  for(let i=0;i<tempArray.length;i++){// Iterate over the temporary array.
    if(!(((tempArray[i]>=tempArray[i+1])&&(tempArray[i+1]<arr[i])))){ // If the element in the current position of the list is greater than or equal to its immediate successor and lesser than the element at that index, then don't allow this operation.
      return false;//Return False if the condition