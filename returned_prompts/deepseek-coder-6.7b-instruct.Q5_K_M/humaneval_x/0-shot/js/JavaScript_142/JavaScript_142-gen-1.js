  let sum = 0;
  for(let i = 0; i < lst.length; i++){
    if(i % 3 == 0 && i % 4 != 0){
      sum += lst[i] ** 2;
    } else if (i % 4 == 0){
      sum += lst[i] ** 3;
    } else {
      sum += lst[i];
    }
  }
  return sum;
}
console.log(sumSquares([1,2,3])); // 6
console.log(sumSquares([])); // 0
console.log(sumSquares([-1,-5,2,-1,-5])); // -126

*/

// This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
// multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
// change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 

function sumSquares(lst) {
  let sum = 0;
  for(let i = 0; i < lst.length; i++){
    if(i % 3 == 0 && i % 4 != 0){
      sum += lst[i] ** 2;
    } else if (i % 4 == 0){
      sum += lst[i] ** 3;
    } else {
      sum += lst[i];
    }
  }
  return sum;
}
console.log(sumSquares([1,2,3])); // 6
console.log(sumSquares([])); // 0
console.log(sumSquares([-1,-5,2,-1,-5])); // -126
