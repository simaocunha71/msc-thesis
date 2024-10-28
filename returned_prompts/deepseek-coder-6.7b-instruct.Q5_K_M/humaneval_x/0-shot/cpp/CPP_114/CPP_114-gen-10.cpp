    long long ans = LLONG_MAX;
    long long sum = 0;
    for(int i = 0; i < nums.size(); i++){
        sum += nums[i];
        ans = min(ans, sum);
        if(sum > 0){
            sum = 0;
        }
    }
    return ans;
}

int main(){
    vector<long long> nums = {2, 3, -4, 1, -2, 4};
    printf("%lld\n", minSubArraySum(nums));
    return 0;
}
*/

//cpp/problem_solving/minimum_subarray_sum_2.cpp
#include <stdio.h>
#include <vector>
#include <climits>
using namespace std;

long long minSubArraySum(vector<int> nums){
    long long ans = LLONG_MAX;
    long long sum = 0;
    for(int i = 0; i < nums.size(); i++){
        sum += nums[i];
        ans = min(ans, sum);
        if(sum > 0){
            sum = 0;
        }
    }
    return ans;
}

int main(){
    vector<int> nums = {2, 3, -4, 1, -2, 4};
    printf("%lld\n", minSubArraySum(nums));
    return 0;
}

//cpp/problem_solving/minimum_subarray_sum_3.cpp
#include <stdio.h>
#include <vector>
#include <climits>
using namespace std;

long long minSubArraySum(vector<int> nums){
    long long ans = LLONG_MAX;
    long long sum = 0;
    for(int i = 0; i < nums.size(); i++){
        sum += nums[i];
        ans = min(ans, sum);
        if(sum > 0){
            sum = 0;
        }
    }
    return ans;
}

int main(){
    vector<