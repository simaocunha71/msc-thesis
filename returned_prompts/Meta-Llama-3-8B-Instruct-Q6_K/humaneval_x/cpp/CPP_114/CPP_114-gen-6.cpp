long long sum = 0;
long long minSum = LONG_LONG_MAX;
for(int i = 0; i < nums.size(); i++){
    sum = 0;
    for(int j = i; j < nums.size(); j++){
        sum += nums[j];
        if(sum < minSum){
            minSum = sum;
        }
    }
}
return minSum;
}
int main(){
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    printf("minSubArraySum is %lld\n", minSubArraySum(nums));
    return 0;
}

Answer:
The time complexity of this solution is O(n^2) because for each element in the array, we are iterating over the rest of the array.
Here is a more efficient solution with a time complexity of O(n):

```cpp
#include<stdio.h>
#include<vector>
using namespace std;
long long minSubArraySum(vector<long long> nums){
    long long minSum = nums[0];
    long long currentSum = nums[0];
    for(int i = 1; i < nums.size(); i++){
        currentSum = min(nums[i], currentSum + nums[i]);
        minSum = min(minSum, currentSum);
    }
    return minSum;
}
int main(){
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    printf("minSubArraySum is %lld\n", minSubArraySum(nums));
    return 0;
}
```
In this solution, we initialize `minSum` to the first element of the array and `currentSum` to the first element of the array. Then, for each element in the array starting from the second element, we update `currentSum` to be the minimum of the current element and the sum of the current element and `currentSum`. We also update `minSum` to be the minimum of `minSum` and `currentSum`. This way, `minSum` will always store the minimum sum of a non-empty sub-array ending at the current position. The time complexity of this solution is O(n) because we are only iterating over the array once.