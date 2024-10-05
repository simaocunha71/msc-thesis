/*
  let count = 0;
  for(let i = 0; i < nums.length; i++){
    if(nums[i] > 10 && (nums[i] % 10) % 2 !== 0 && (nums[i] % 100) % 10 !== 0){
      count++
    }
  }
  return count;
*/

  return nums.filter((num) => num > 10 && (num % 10) % 2 !== 0 && (num % 100) % 10 !== 0).length;
}
