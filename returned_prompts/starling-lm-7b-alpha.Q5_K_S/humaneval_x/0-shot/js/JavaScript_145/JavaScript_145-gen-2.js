const orderByPoints = (nums) => {
  const arr = nums.map((num, index) => ({
    num,
    index
  }));
  return arr.sort((a, b) => {
    const sumA = a.num.toString().split('').reduce((sum, num) => sum + +num, 0);
    const sumB = b.num.toString().split('').reduce((sum, num) => sum + +num, 0);
    if (sumA === sumB) {
      return a.index - b.index;
    }
    return sumA - sumB;
  });
};

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
  const arr = nums.map((num, index) => ({
    num,
    index
  }));
  return arr.sort((a, b) => {
    const sumA = a.num.toString().split('').reduce((sum, num) => sum + +num, 0);
    const sumB = b.num.toString().split('').reduce((sum, num) => sum + +num, 0);
    if (sumA === sumB) {
      return a.index - b.index;
    }
    return sumA - sumB;
  });
};






















*/
orderByPoints([1, 11, -1, -11, -12])
orderByPoints([])






































