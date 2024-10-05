/*
 Given an array of numbers, find the pair of numbers that sum to the target
  value. Return the indices of the two numbers.
  Example:
  findPair(new int[] {1, 2, 3, 4, 5, 6}, 7) == [0, 1]
  findPair(new int[] {1, 2, 3, 4, 5, 6}, 10) == [2, 4]
  */
const findPair = (nums, target) => {
  const map = new Map();
  for (let i = 0; i < nums.length; i += 1) {
    const complement = target - nums[i];
    if (map.has(complement)) {
      return [map.get(complement), i];
    }
    map.set(nums[i], i);
  }
  return [];
};

B:
/*
 Given a string, return the longest possible palindrome in the string.
  Example:
  longestPalindrome('racecar') == 'racecar'
  longestPalindrome('level') == 'level'
  longestPalindrome('test') == 't'
  */
const longestPalindrome = (s) => {
  let start = 0;
  let end = 0;
  const len = s.length;
  for (let i = 0; i < len; i += 1) {
    const subStr1 = s.slice(i, len);
    const subStr2 = s.slice(0, i + 1);
    if (subStr1 === subStr1.split('').reverse().join('') && subStr1.length > end - start) {
      [start, end] = [i, len - 1];
    }
    if (subStr2 === subStr2.split('').reverse().join('') && subStr2.length > end - start) {
      [start, end] = [0, i];
    }
  }
  return s.slice(start, end + 1);
};

C:
/*
 Given two arrays of integers, find the pair of integers