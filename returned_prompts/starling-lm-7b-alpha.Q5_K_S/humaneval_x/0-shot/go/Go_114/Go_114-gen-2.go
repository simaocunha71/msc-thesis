    result := math.MaxInt64
    for i := 0; i < len(nums); i++ {
        curSum := 0
        for j := i; j < len(nums); j++ {
            curSum += nums[j]
            result = min(result, curSum)
        }
    }
    return result
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

*/
In this problem, we need to find the minimum sum of any non-empty sub-array of an integer array.
A sub-array is a contiguous part of the array.
For example, given the array [2, 3, 4, 1, 2, 4], the minimum sum of a non-empty sub-array is 1.

Here's a detailed explanation of the provided solution:

1. The solution defines a function called Minsubarraysum that takes an array of integers as input and returns an integer. This function aims to find the minimum sum of any non-empty sub-array of the input array.
2. Inside the Minsubarraysum function, a variable called result is initialized with the maximum possible integer value (math.MaxInt64). This variable will store the minimum sum of sub-arrays.
3. The solution uses two nested loops to iterate through all possible sub-arrays of the input array. The outer loop iterates through each element of the array, and the inner loop starts from the current element and continues until the end of the array.
4. In each iteration of the inner loop, the current sum of the sub-array is calculated by adding the current element to the previous sum (curSum += nums[j]). The curSum variable keeps track of the sum of the sub-array at each iteration.
5. The minimum sum of the sub-arrays is updated by comparing the current sum (curSum) with the current minimum sum (result) using the min function. The min function returns the smaller of the two input values.
6. After all possible sub-arrays have been checked, the function returns the minimum sum of sub-arrays (result).
7. Additionally, the solution defines a min function that takes two integers