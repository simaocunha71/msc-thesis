    long long sum = 0;
    long long minSum = nums[0];
    for(int i = 0; i < nums.size(); i++){
        sum += nums[i];
        if(sum < minSum)
            minSum = sum;
        if(sum > 0)
            sum = 0;
    }
    return minSum;
}
int main() {
    vector<long long> nums = {2, 3, -4, 1, -2, 4};
    printf("%lld\n", minSubArraySum(nums));
    return 0;
}

*/
#include<stdio.h>
#include<vector>
using namespace std;
long long minSubArraySum(vector<long long> nums){
    long long sum = 0;
    long long minSum = nums[0];
    for(int i = 0; i < nums.size(); i++){
        sum += nums[i];
        if(sum < minSum)
            minSum = sum;
        if(sum > 0)
            sum = 0;
    }
    return minSum;
}
int main() {
    vector<long long> nums = {2, 3, -4, 1, -2, 4};
    printf("%lld\n", minSubArraySum(nums));
    return 0;
}

// The function minSubArraySum calculates the smallest non-negative sum in the subarray.
// If all numbers are negative, then the smallest sum is the largest one (the smallest sum of an empty subarray).
// The function uses a dynamic programming approach, where the variable sum keeps track of the current sum. 
// If sum is negative, the variable minSum keeps track of the smallest sum.
// The function iterates over the array, adding each number to sum. If sum becomes negative, it is reset to 0.
// After iterating, the function returns the smallest sum, which is the minimum sum of any non-empty sub-vector of nums.
// The function has a time complexity of O(n), where n is the size of the input vector.
// The function has a space complexity of O(