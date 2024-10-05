    let res = [];

    arr.sort((a, b) => b - a);

    for (let i = 0; i < k; i++) {
        res.push(arr[i]);
    }

    return res;
};

console.log(maximum([-3, -4, 5], 3));
console.log(maximum([4, -4, 4], 2));
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1));
*/



/*
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to k. Please return the length of that subarray.

Example:

Input: nums = [1,2,3,4], k = 3
Output: 2
Explanation: The longest subarray is [2,3] with length 2.

Input: nums = [1,2,3], k = 3
Output: 3
Explanation: The longest subarray is the whole array with length 3.

Input: nums = [1,2,3,4,5], k = 4
Output: 4
Explanation: The longest subarray is [1,2,3,4] with length 4.

Note:

The length of the array is between 1 and 20,000.
The absolute difference between any two elements in the subarray is less than or equal to k.

*/



/*
Given an integer array as strings, you need to return a new string array length of the original array multiplied by 2.

The new array will have a k-alternating pattern:

1. The first k elements of the new array will contain all the even elements from the original array. They have to be in the same order as in the original array.

2. The last k elements of the new array will contain all the odd elements from the original array. They have to be in the same order as in the original array.

The first element of the original array should be the first element of the new array, and thus of the same string