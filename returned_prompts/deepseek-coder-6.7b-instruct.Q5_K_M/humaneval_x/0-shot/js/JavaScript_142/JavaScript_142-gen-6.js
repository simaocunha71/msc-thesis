let sum = 0;
  
for(let i = 0; i < lst.length; i++){
  if(i % 3 === 0 && i % 4 !== 0){
    sum += lst[i] * lst[i]
  } else if(i % 4 === 0){
    sum += lst[i] * lst[i] * lst[i]
  } else {
    sum += lst[i]
  }
}

return sum;
};



// TEST CASES:
console.log(sumSquares([1,2,3])); // 6
console.log(sumSquares([])); // 0
console.log(sumSquares([-1,-5,2,-1,-5])); // -126






//Solution: 
/*
The function sumSquares goes through the list of integers checking if the index is a multiple of 3 and not 4, if it is, it squares the 
integer and adds it to the sum. If the index is a multiple of 4, it cubes the integer and adds it to the sum. If the index is not a 
multiple of 3 or 4, the function leaves the integer as is and adds it to the sum. Finally, the function returns the total sum.
*/



































































































































































































