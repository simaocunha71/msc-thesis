  let count = 0;
  const isOdd = num => num % 2 !== 0;
  const firstLastOdd = num => isOdd(parseInt(num.toString().charAt(0))) && isOdd(parseInt(num.toString().charAt(num.toString().length - 1)));

  for(let i = 0; i < nums.length; i++){
    if(nums[i] > 10 && firstLastOdd(nums[i])){
      count++;
    }
  }
  return count;
}
console.log(specialFilter([15, -73, 14, -15])); // 1
console.log(specialFilter([33, -2, -3, 45, 21, 109])); // 2

*/

*/

function specialFilter(nums){
    let count = 0;
    const isOdd = num => num % 2 !== 0;
    const firstLastOdd = num => isOdd(parseInt(num.toString().charAt(0))) && isOdd(parseInt(num.toString().charAt(num.toString().length - 1)));

    for(let i = 0; i < nums.length; i++){
        if(nums[i] > 10 && firstLastOdd(nums[i])){
            count++;
        }
    }
    return count;
}
console.log(specialFilter([15, -73, 14, -15])); // 1
console.log(specialFilter([33, -2, -3, 45, 21, 109])); // 2



/* 
1. I defined a function specialFilter that takes an array of numbers as argument.
2. I defined a helper function isOdd that checks if a number is odd.
3. I defined another helper function firstLastOdd that checks if the first and last digits of a number are odd.
4. I initialize a counter to 0.
5. I loop over the input array and for each element:
   - I check if the