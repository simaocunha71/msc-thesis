  let minSum = Infinity;
  let curSum = 0;
  
  for (let num of nums) {
    curSum = Math.min(curSum + num, num);
    minSum = Math.min(minSum, curSum);
  }
  
  return minSum;
};

console.log(minSubArraySum([2, -3, 4, -1, 2, 4])); // -6
console.log(minSubArraySum([3, -2, 4, -1, 2, -4])); // -8
console.log(minSubArraySum([-1, -2, -3])); // -6
console.log(minSubArraySum([1, 2, 3])); // 6
console.log(minSubArraySum([2, 3, 4, 1, 2, 4])); // 1
console.log(minSubArraySum([1])); // 1

*/

const minSubArraySum = (nums) => {
  let minSum = Infinity;
  let curSum = 0;

  for (let num of nums) {
    curSum = Math.min(curSum + num, num);
    minSum = Math.min(minSum, curSum);
  }

  return minSum;
};

console.log(minSubArraySum([2, -3, 4, -1, 2, 4])); // -6
console.log(minSubArraySum([-1, -2, -3])); // -6
console.log(minSubArraySum([1, 2, 3])); // 6
console.log(minSubArraySum([2, 3, 4, 1, 2, 4])); // 1
console.log(minSubArraySum([1])); // 1

/*
