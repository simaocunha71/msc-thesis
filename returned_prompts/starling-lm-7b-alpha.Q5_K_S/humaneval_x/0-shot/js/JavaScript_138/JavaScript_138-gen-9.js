    let sum = 0;
    let i = 2;
    while(sum < n && i < n){
        sum += i;
        i += 2;
    }
    return sum === n;
};

console.log(isEqualToSumEven(4)); // false
console.log(isEqualToSumEven(6)); // false
console.log(isEqualToSumEven(8)); // true
console.log(isEqualToSumEven(9)); // false
console.log(isEqualToSumEven(10)); // true

*/

/*
Given an array of positive numbers and a positive number k, find the maximum sum of a contiguous subarray of size k in the array.

Example:

getMaxSum(1, [1, 2, 3, 4, 5]) -> 8
Explanation: The subarray with the greatest sum is [3, 4, 5].

getMaxSum(2, [1, 2, 3, 4, 5]) -> 8
Explanation: The subarray with the greatest sum is [2, 3].

getMaxSum(3, [1, 2, 3, 4, 5]) -> 12
Explanation: The subarray with the greatest sum is [2, 3, 4].

getMaxSum(4, [1, 2, 3, 4, 5]) -> 12
Explanation: The subarray with the greatest sum is [2, 3, 4].

getMaxSum(5, [1, 2, 3, 4, 5]) -> 15
Explanation: The subarray with the greatest sum is [2, 3, 4, 5].

Note:
The size of the array and k will not exceed 10^6.
*/

function getMaxSum(k, nums) {
    let max = 0;
    let sum = 0;
    for (let i = 0; i < k; i++) {
        sum += nums[i];
    }
    max = sum;
    for (let i = k; i < nums.length;