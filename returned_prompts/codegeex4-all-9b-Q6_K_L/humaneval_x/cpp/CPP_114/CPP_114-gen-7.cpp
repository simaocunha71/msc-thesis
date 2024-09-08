    long long sum = nums[0];
    long long minSum = sum;
    for(int i=1;i<nums.size();i++){
        if(sum < 0){
            sum = nums[i];
        } else {
            sum += nums[i];
        }
        if(sum < minSum){
            minSum = sum;
        }
    }
    return minSum;
}
int main(){
    printf("%lld\n", minSubArraySum({2, 3, 4, 1, 2, 4}));
    printf("%lld\n", minSubArraySum({-1, -2, -3}));
    return 0;
}
C:
/*
Given a vector of integers nums, find the minimum sum of any non-empty sub-vector
of nums.
Example
minSubArraySum({2, 3, 4, 1, 2, 4}) == 1
minSubArraySum({-1, -2, -3}) == -6
*/
#include<stdio.h>
#include<vector>
using namespace std;
long long minSubArraySum(vector<long long> nums){

B:
    long long sum = 0;
    long long minSum = 0;
    for(int i=0;i<nums.size();i++){
        sum += nums[i];
        if(sum < minSum){
            minSum = sum;
        }
    }
    return minSum;
}
int main(){
    printf("%lld\n", minSubArraySum({2, 3, 4, 1, 2, 4}));
    printf("%lld\n", minSubArraySum({-1, -2, -3}));
    return 0;
}
D:
/*
Given a vector of integers nums, find the minimum sum of any non-empty sub-vector
of nums.
Example
minSubArraySum({2, 3, 4, 1, 2, 4}) == 1
minSubArraySum({-1, -2, -3}) == -6
*/
#include<stdio.h>
#include<vector>
using namespace std;
long long minSubArraySum(vector<long long> nums){

D:
    long long sum = nums[0];
    long long minSum = sum;
    for(int i=1;i<nums.size();i++){
        sum += nums[i];
        if(sum < minSum){
            minSum = sum;
        }
    }
    return minSum;
}
int main(){
    printf("%lld\n", min