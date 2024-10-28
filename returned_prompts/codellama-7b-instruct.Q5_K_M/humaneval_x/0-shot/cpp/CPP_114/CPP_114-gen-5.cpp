    int size = nums.size();
    vector<long long> dp(size, 0);
    dp[0] = nums[0];
    for (int i = 1; i < size; i++){
        dp[i] = dp[i-1] + nums[i];
    }
    long long min = nums[0];
    for (int i = 0; i < size; i++){
        for (int j = i; j < size; j++){
            long long sum = dp[j] - dp[i-1];
            if (sum < min)
                min = sum;
        }
    }
    return min;
}
int main(){
    vector<long long> nums = {-1, -2, -3};
    printf("%lld\n", minSubArraySum(nums));
    return 0;
}

B:

#include<stdio.h>
#include<vector>
using namespace std;
long long minSubArraySum(vector<long long> nums){

    int size = nums.size();
    vector<long long> dp(size, 0);
    dp[0] = nums[0];
    for (int i = 1; i < size; i++){
        dp[i] = dp[i-1] + nums[i];
    }
    long long min = nums[0];
    for (int i = 0; i < size; i++){
        long long sum = 0;
        for (int j = i; j < size; j++){
            sum += dp[j] - dp[i-1];
            if (sum < min)
                min = sum;
        }
    }
    return min;
}
int main(){
    vector<long long> nums = {-1, -2, -3};
    printf("%lld\n", minSubArraySum(nums));
    return 0;
}

C:

#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
long long minSubArraySum