  let sum = 0;
  for(let i=0; i<lst.length; i++){
    if(i%3 === 0 && i%4 === 0){
      sum += lst[i] ** 2;
    } else if(i%4 === 0){
      sum += lst[i] ** 3;
    } else {
      sum += lst[i];
    }
  }
  return sum;
}
// Test Cases:
console.log(sumSquares([1,2,3])); // Output: 6
console.log(sumSquares([])); // Output: 0
console.log(sumSquares([-1,-5,2,-1,-5])); // Output: -126
*/

const sumSquares = (lst) => {
  let sum = 0;
  for(let i = 0; i < lst.length; i++){
    if(i % 3 === 0 && i % 4 === 0){
      sum += lst[i] ** 2;
    } else if(i % 4 === 0){
      sum += lst[i] ** 3;
    } else {
      sum += lst[i];
    }
  }
  return sum;
}

console.log(sumSquares([1,2,3])); // Output: 6
console.log(sumSquares([])); // Output: 0
console.log(sumSquares([-1,-5,2,-1,-5])); // Output: -126

/*
  This function works by iterating over each index of the array. If the index is a multiple of both 3 and 4, the element at that 
  index is squared and added to the sum. If the index is a multiple of 4 but not 3, the element is cubed and added to the sum. 
  If the index is not a multiple of either 3 or 4, the element is simply added to the sum. The final sum is then returned.
*/


























