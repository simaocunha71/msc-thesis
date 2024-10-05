  let even = 0, odd = 0;
  let nums = Math.abs(num).toString().split('');

  for(let i = 0; i < nums.length; i++){
    if(nums[i] % 2 == 0)
      even++;
    else
      odd++;
  }

  return [even, odd];
}



