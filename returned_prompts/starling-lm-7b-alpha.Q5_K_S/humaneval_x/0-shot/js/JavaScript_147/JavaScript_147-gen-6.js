const a = [];
for(let i=1;i<=n;i++) a.push(i*i - i + 1);
let count = 0;

for(let i=0;i<a.length;i++){
    for(let j=i+1;j<a.length;j++){
        for(let k=j+1;k<a.length;k++){
            if((a[i] + a[j] + a[k]) % 3 === 0){
                count++;
            }
        }
    }
}

return count;

};



/*
  You are given an integer array nums. You have to find three
  self overlapping palindromes on this array. Return the length of the longest palindrome.
  You can assume that the length of the array is at most 20. The array length will be odd.
  Note: A self overlapping palindrome is a palindrome where the first and last letters
  in the sequence overlap by one position. For example, "aba" is a palindrome,
  but "abaacb" is not.

  Example :
      Input: nums = [1, 2, 3, 4, 5]
      Output: 5

      Explanation:
      Here are the three self overlapping palindromes we can find:
      "123321", "23323" and "33233".

  Note :
      Length of the array is at most 20
      The array length will be odd.

  Constraints:
      3 <= length of nums <= 20
*/
const findLongestPalindrome = (nums) => {

    let max = 1;
    for(let i=0;i<nums.length;i++){
        for(let j=i+1;j<nums.length;j++){
            for(let k=j+1;k<nums.length;k++){
                if(nums[i] === nums[j] && nums[j] === nums[k] &&
                    nums[i