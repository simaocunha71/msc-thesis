/*
  The easiest way to solve this problem is to iterate over the numbers from x to y and check if each number is even and in the range.
  The time complexity of this solution is O(n) where n is the range between x and y.

  The space complexity of this solution is O(1) because we don't use any extra memory.

  But can we do better?
*/

B:
/*
  Let's think about what we really need to find. We need to find the biggest even number in the range [x, y] inclusive.
  So we only need to check if each number is even and in the range.

  So the solution will be:
*/
const chooseNum = (x, y) => {
  let max = -1;
  for (let i = x; i <= y; i++) {
    if (i % 2 === 0 && i >= x && i <= y) {
      max = i;
    }
  }
  return max;
};

