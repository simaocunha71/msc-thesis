    if(s.length < 3) return false;
    const arr = s.split('');
    for(let i = 0; i < arr.length - 2; i++) {
        const str = arr.slice(i, i+3).join('');
        if(arr.slice(i+1, i+3).join('') === str) {
            return false;
        }
    }
    return true;
}

console.log(isHappy('abcd'));





/*
  Given a string, you have to find out the length of the longest substring in which all the characters are unique.
  For example:
  lengthOfLongestSubstring('abcabcbb') => 3
  lengthOfLongestSubstring('bbbbbb') => 1
  lengthOfLongestSubstring('pwwkew') => 3
  lengthOfLongestSubstring('') => 0
  lengthOfLongestSubstring('a') => 1
  */
const lengthOfLongestSubstring = (s) => {
    let result = 0;
    let str = '';
    for(let i = 0; i < s.length; i++) {
        if(str.indexOf(s[i]) === -1) {
            str += s[i];
            result = Math.max(result, str.length);
        } else {
            str = str.substring(str.indexOf(s[i]) + 1) + s[i];
        }
    }
    return result;
}

console.log(lengthOfLongestSubstring('abcabcbb'));



/*
  Given an array of integers, find the maximum sum of a subarray within the array.
  For example:
  maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) => 6
  maxSubArray([1]) => 1
  maxSubArray([5, 4, -1, 7, 8]) => 23
  */
const maxSubArray = (nums) => {
    let result = nums[0];
    let cur = 0;
    for(let