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
  if(array.length === 0){
    return array;
  }

  // O(n)
  let sum=0;
  let newArray=[];
  
  for(let i=0,j=array.length-1;i<j;i++){
    sum += parseInt(array[i]);
    console.log("sum = "+parseInt(array[i])+", "+parseInt(array[j]));
    if (sum%2===0){
      newArray.push(parseInt(array[i])*(-1));
    }else{
      newArray.push(parseInt(array[i]));
    }
  }
  console.log("newArray = "+newArray.join(", "))
  
  return newArray;
}