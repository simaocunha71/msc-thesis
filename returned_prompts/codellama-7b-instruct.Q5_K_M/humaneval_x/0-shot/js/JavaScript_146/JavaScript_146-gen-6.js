
function specialFilter(nums){

  let count = 0;

  for(let i = 0; i < nums.length; i++){

    if(nums[i] > 10){

      let str = nums[i].toString();

      if(str[0] % 2 === 1 && str[str.length - 1] % 2 === 1){

        count++;

      }

    }

  }

  return count;

}







