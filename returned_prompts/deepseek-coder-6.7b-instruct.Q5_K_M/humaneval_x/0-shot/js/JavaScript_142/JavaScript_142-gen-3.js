  let sum = 0;
  for(let i=0; i<lst.length; i++){
    if(i%3 === 0){
      sum += Math.pow(lst[i], 2);
    } else if(i%4 === 0){
      sum += Math.pow(lst[i], 3);
    } else {
      sum += lst[i];
    }
  }
  return sum;
}
*/

const sumSquares = (lst) => {

  let sum = 0;
  for(let i=0; i<lst.length; i++){
    if(i%3 === 0){
      sum += Math.pow(lst[i], 2);
    } else if(i%4 === 0){
      sum += Math.pow(lst[i], 3);
    } else {
      sum += lst[i];
    }
  }
  return sum;
}

console.log(sumSquares([1,2,3])); // should return 6
console.log(sumSquares([])); // should return 0
console.log(sumSquares([-1,-5,2,-1,-5])); // should return -126

// The function works as expected. It iterates over the input array and checks the index of each element. If the index is a multiple of 3, 
// it squares the element and adds it to the sum. If the index is a multiple of 4 and not a multiple of 3, it cubes the element and adds it to the sum. 
// For all other indices, it simply adds the element to the sum.
// The function returns the sum of all elements after the iterations are complete.
// This function assumes that the input array will only contain integers. If this is not the case, additional error handling may be needed.
// The function also assumes that the indices of the array start at 0, which is a common convention in many programming languages.
// If the indices start at a different value, the function will need to be adjusted accordingly.



























