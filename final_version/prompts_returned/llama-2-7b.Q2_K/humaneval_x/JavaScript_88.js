/*
  Given an array of non-negative integers, return a copy of the given array after sorting,
  you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
  or sort it in descending order if the sum( first index value, last index value) is even.

  Note:
  * don't change the given array.

  Examples:
  * sortArray([]) => []
  * sortArray([5]) => [5]
  * sortArray([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
  * sortArray([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
  */
const sortArray = (array) => {
  if(array.length === 0) return array;
    
  let sum = 0;   // sum of all items in array
  for (let i=0;i<array.length;++i){
    sum += array[i];
  }

  switch (sum % 2 ) { // modulo is how to get the remainder after division by a number
    case 1:
      sortArray(array).reverse();
      break; // swap array and reverse it, if odd
      
    default:
      break; // normal sorting otherwise, else fall through
  }
  return sortArray(array);
}
