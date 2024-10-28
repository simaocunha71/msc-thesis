let count = 0;
for(let i=11; i<n; i++){
  if(i%11 === 0 || i%13 === 0){
    count += (i.toString().match(/7/g) || []).length;
  }
}
return count;
}

//Test Cases
console.log(fizzBuzz(50));  //0
console.log(fizzBuzz(78));  //2
console.log(fizzBuzz(79));  //3

*/

// 5. Given an array of integers, return indices of the two numbers such that they add up to a specific target.

/*
