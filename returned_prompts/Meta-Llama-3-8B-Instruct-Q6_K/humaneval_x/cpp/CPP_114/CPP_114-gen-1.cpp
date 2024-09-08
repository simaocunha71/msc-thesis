The problem asks to find the minimum sum of any non-empty sub-vector of the given vector of integers. This can be achieved by using Kadane's algorithm which is used to find the maximum sum of a sub-array within a one-dimensional array of numbers.

The idea behind this algorithm is to keep track of the maximum sum of a sub-array ending at each position. If the sum becomes negative, we reset it to 0. This ensures that we consider the maximum sum of a sub-array ending at each position.

In this problem, we are asked to find the minimum sum, so we can use the same algorithm but instead of keeping track of the maximum sum, we keep track of the minimum sum.

Here is the implementation of the algorithm:

```cpp
#include<stdio.h>
#include<vector>
using namespace std;

long long minSubArraySum(vector<long long> nums){
    long long minSum = LONG_LONG_MAX;
    long long currentSum = 0;
    for(long long i=0; i < nums.size(); i++){
        currentSum += nums[i];
        minSum = min(minSum, currentSum);
        if(currentSum > 0) {
            currentSum = 0;
        }
    }
    return minSum;
}

int main()
{
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    printf("%lld\n", minSubArraySum(nums));
    return 0;
}
```

In this code, we initialize `minSum` to `LONG_LONG_MAX` and `currentSum` to 0. Then we iterate through the vector and add each element to `currentSum`. We update `minSum` if `currentSum` is less than `minSum`. If `currentSum` becomes