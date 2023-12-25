/*
  Write a function which sorts the given list of integers
  in ascending order according to the sum of their digits.
  Note: if there are several items with similar sum of their digits,
  order them based on their index in original list.

  For example:
  >>> orderByPoints([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
  >>> orderByPoints([]) == []
  */
const orderByPoints = (nums) => {
  const list = nums.sort((a, b) => a.digitSum <= b.digitSum ? 1 : -1);
  for (let i = 0; i < nums.length; ++i) {
    if (i !== 0 && nums[i].index === undefined) {
      throw new Error('Index must be defined at position ' + i);
    } else {
      nums[i - 1] = nums[i];
    }
  }
  return list;
};
