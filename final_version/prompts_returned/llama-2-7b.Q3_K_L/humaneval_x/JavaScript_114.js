/*
  Given an array of integers nums, find the minimum sum of any non-empty sub-array
  of nums.
  Example
  minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
  minSubArraySum([-1, -2, -3]) == -6
  */
const minSubArraySum = (nums) => {
  const array = nums.slice();
  let result;
  function findMin(array, startIndex = 0, endIndex) {
    if (startIndex === array.length || endIndex === array.length) return result;
    if (array[endIndex] < 0) endIndex++;
    for (let index = startIndex + 1; index <= endIndex; index++) {
      const sum = array[index];
      if (!sum || !(sum >= 0)) continue;
      result = findMin([...array, sum], startIndex, index);
      break;
    }
    return result;
  }
  let sum = Math.abs(findMin(array));
  for (let i = 1; i < array.length - 1; i++) {
    if (i === 0) continue;
    const currentSum = findMin([...array, [sum], ...array]);
    result = Math.min(currentSum, sum);
    sum -= currentSum;
  }
  return result || Infinity;
};
