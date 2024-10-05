
function minSubArraySum(nums) {
  // if (nums.length === 1) return nums[0];
  // let min = nums[0];
  // let sum = 0;
  // for (let i = 0; i < nums.length; i++) {
  //   sum += nums[i];
  //   min = Math.min(min, sum);
  // }
  // return min;

  // let sum = 0;
  // let min = Infinity;
  // for (let i = 0; i < nums.length; i++) {
  //   sum += nums[i];
  //   min = Math.min(min, sum);
  //   if (sum < 0) {
  //     sum = 0;
  //   }
  // }
  // return min;

  let sum = 0;
  let min = Infinity;
  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    min = Math.min(min, sum);
    if (sum < 0) {
      sum = nums[i];
    }
  }
  return min;
}

let nums = [-1, -2, -3];
console.log(minSubArraySum(nums));
